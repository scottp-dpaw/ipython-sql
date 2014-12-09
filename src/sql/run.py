import functools
import operator
import types
import csv
import six
import codecs
import os.path
import sqlalchemy
import sqlparse
import prettytable
from .column_guesser import ColumnGuesserMixin

from .qgis import qgis_generate

def unduplicate_field_names(field_names):
    """Append a number to duplicate field names to make them unique. """
    res = []
    for k in field_names:
        if k in res:
            i = 1
            while k + '_' + str(i) in res:
                i += 1
            k += '_' + str(i)
        res.append(k)
    return res

class UnicodeWriter(object):
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = six.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        if six.PY2:
            _row = [s.encode("utf-8")
                    if hasattr(s, "encode")
                    else s
                    for s in row]
        else:
            _row = row
        self.writer.writerow(_row)
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        if six.PY2:
           data = data.decode("utf-8")
           # ... and reencode it into the target encoding
           data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
        self.queue.seek(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

class CsvResultDescriptor(object):
    """Provides IPython Notebook-friendly output for the feedback after a ``.csv`` called."""
    def __init__(self, file_path):
        self.file_path = file_path
    def __repr__(self):
        return 'CSV results at %s' % os.path.join(os.path.abspath('.'), self.file_path)
    def _repr_html_(self):
        return '<a href="%s">CSV results</a>' % os.path.join('.', 'files', self.file_path)

class QgisProjectDescriptor(object):
    """Provides IPython Notebook-friendly output for the feedback after a ``.qgis`` called."""
    def __init__(self, file_path):
        self.file_path = file_path
    def __repr__(self):
        return 'QGIS project at %s' % os.path.join(os.path.abspath('.'), self.file_path)
    def _repr_html_(self):
        return '<a href="%s">QGIS project</a>' % os.path.join('.', 'files', self.file_path)


class ResultSet(list, ColumnGuesserMixin):
    """
    Results of a SQL query.
    
    Can access rows listwise, or by string value of leftmost column.
    """
    def __init__(self, sqlaproxy, sql, conn, config):
        self.keys = sqlaproxy.keys()
        self.sql = sql
        self.conn = conn
        self.config = config
        self.limit = config.autolimit
        style_name = config.style
        self.style = prettytable.__dict__[style_name.upper()]
        if sqlaproxy.returns_rows:
            # determine which columns have raw PostGIS data in them
            #gisfilter = [i for i in range(len(self.field_names)) if self.field_names[i] in ('geom', 'the_geom')]
            gisfilter = [i for i in range(len(sqlaproxy.cursor.description)) if sqlaproxy.cursor.description[i].type_code in (563391,)]
            
            if self.limit:
                list.__init__(self, sqlaproxy.fetchmany(size=self.limit))
            else:
                list.__init__(self, sqlaproxy.fetchall())
            self.field_names = unduplicate_field_names(self.keys)
            self.pretty = prettytable.PrettyTable(self.field_names)
            

            if not config.autopandas:
                for row in self[:config.displaylimit or None]:
                    prettyrow = [r for r in row]
                    # remove PostGIS data for HTML view
                    for i in gisfilter:
                        prettyrow[i] = 'GIS data, {} bytes'.format(len(prettyrow[i]))
                    self.pretty.add_row(prettyrow)
            self.pretty.set_style(self.style)
        else:
            list.__init__(self, [])
            self.pretty = None
    def _repr_html_(self):
        if self.pretty:
            result = self.pretty.get_html_string()
            if self.config.displaylimit and len(self) > self.config.displaylimit:
                result = '%s\n<span style="font-style:italic;text-align:center;">%d rows, truncated to displaylimit of %d</span>' % (
                    result, len(self), self.config.displaylimit)
            return result
        else:
            return None
    def __str__(self, *arg, **kwarg):
        return str(self.pretty or '')
    def __getitem__(self, key):
        """
        Access by integer (row position within result set)
        or by string (value of leftmost column)
        """
        try:
            return list.__getitem__(self, key)
        except TypeError:
            result = [row for row in self if row[0] == key]
            if not result:
                raise KeyError(key)
            if len(result) > 1:
                raise KeyError('%d results for "%s"' % (len(result), key))
            return result[0]
    def DataFrame(self):
        "Returns a Pandas DataFrame instance built from the result set."
        import pandas as pd
        frame = pd.DataFrame(self, columns=(self and self.keys) or [])
        return frame
    def pie(self, key_word_sep=" ", title=None, **kwargs):
        """Generates a pylab pie chart from the result set.
       
        ``matplotlib`` must be installed, and in an
        IPython Notebook, inlining must be on::
        
            %%matplotlib inline
            
        Values (pie slice sizes) are taken from the 
        rightmost column (numerical values required).
        All other columns are used to label the pie slices.
        
        Parameters
        ----------
        key_word_sep: string used to separate column values
                      from each other in pie labels
        title: Plot title, defaults to name of value column

        Any additional keyword arguments will be passsed 
        through to ``matplotlib.pylab.pie``.
        """
        self.guess_pie_columns(xlabel_sep=key_word_sep)
        import matplotlib.pylab as plt
        pie = plt.pie(self.ys[0], labels=self.xlabels, **kwargs)
        plt.title(title or self.ys[0].name)
        return pie
  
    def plot(self, title=None, **kwargs):
        """Generates a pylab plot from the result set.
       
        ``matplotlib`` must be installed, and in an
        IPython Notebook, inlining must be on::
        
            %%matplotlib inline
           
        The first and last columns are taken as the X and Y
        values.  Any columns between are ignored.
        
        Parameters
        ----------
        title: Plot title, defaults to names of Y value columns

        Any additional keyword arguments will be passsed 
        through to ``matplotlib.pylab.plot``.
        """
        import matplotlib.pylab as plt
        self.guess_plot_columns()
        self.x = self.x or range(len(self.ys[0]))
        coords = reduce(operator.add, [(self.x, y) for y in self.ys])
        plot = plt.plot(*coords, **kwargs)
        if hasattr(self.x, 'name'):
            plt.xlabel(self.x.name)
        ylabel = ", ".join(y.name for y in self.ys)
        plt.title(title or ylabel)
        plt.ylabel(ylabel)
        return plot
    
    def bar(self, key_word_sep = " ", title=None, **kwargs):
        """Generates a pylab bar plot from the result set.
       
        ``matplotlib`` must be installed, and in an
        IPython Notebook, inlining must be on::
        
            %%matplotlib inline
           
        The last quantitative column is taken as the Y values;
        all other columns are combined to label the X axis. 
        
        Parameters
        ----------
        title: Plot title, defaults to names of Y value columns
        key_word_sep: string used to separate column values
                      from each other in labels
                      
        Any additional keyword arguments will be passsed 
        through to ``matplotlib.pylab.bar``.
        """
        import matplotlib.pylab as plt
        self.guess_pie_columns(xlabel_sep=key_word_sep)
        plot = plt.bar(range(len(self.ys[0])), self.ys[0], **kwargs)
        if self.xlabels:
            plt.xticks(range(len(self.xlabels)), self.xlabels,
                       rotation=45)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ys[0].name)
        return plot        
    
    def csv(self, filename=None, **format_params):
        """Generate results in comma-separated form.  Write to ``filename`` if given.
           Any other parameters will be passed on to csv.writer."""
        if not self.pretty:
            return None # no results
        if filename:
            encoding = format_params.get('encoding', 'utf-8')
            if six.PY2:
                outfile = open(filename, 'wb')
            else:
                outfile = open(filename, 'w', newline='', encoding=encoding)
        else:
            outfile = six.StringIO()
        writer = UnicodeWriter(outfile, **format_params)
        writer.writerow(self.field_names)
        for row in self:
            writer.writerow(row)
        if filename:
            outfile.close()
            return CsvResultDescriptor(filename)
        else:
            return outfile.getvalue()
    
    def qgis(self, filename, geom_field=None):
        """Generate a QGIS project based on the SQL query, writing it to ``filename``. Optionally, define a column ```geom_field``` to use as a source of GIS data, otherwise fall back on the PostGIS defaults of 'geom' or 'the_geom'."""
        outfile = open(filename, 'wb')
        outfile.write(qgis_generate(self, filename, geom_field))
        outfile.close()
        return QgisProjectDescriptor(filename)
   
def interpret_rowcount(rowcount):
    if rowcount < 0:
        result = 'Done.'
    else:
        result = '%d rows affected.' % rowcount
    return result


def run(conn, sql, config, user_namespace):
    if sql.strip():
        for statement in sqlparse.split(sql):
            txt = sqlalchemy.sql.text(statement)
            result = conn.session.execute(txt, user_namespace)
            if result and config.feedback:
                print(interpret_rowcount(result.rowcount))
        resultset = ResultSet(result, statement, conn, config)
        if config.autopandas:
            return resultset.DataFrame()
        else:
            return resultset
        #returning only last result, intentionally
    else:
        return 'Connected: %s' % conn.name
     
