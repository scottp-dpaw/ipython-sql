QGIS_TEMPLATE = """<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis projectname="" version="2.6.0-Brighton">
    <title></title>
    <layer-tree-group expanded="1" checked="Qt::Checked" name="">
        <customproperties/>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="{layer_id}123456" name="{layer_id}">
            <customproperties/>
        </layer-tree-layer>
    </layer-tree-group>
    <relations/>
    <mapcanvas>
        <units>degrees</units>
        <extent>
            <xmin>112.46224703061122341</xmin>
            <ymin>-35.7851432649286707</ymin>
            <xmax>129.40480653948375789</xmax>
            <ymax>-12.96683817921102921</ymax>
        </extent>
        <projections>0</projections>
        <destinationsrs>
            <spatialrefsys>
                <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
                <srsid>3452</srsid>
                <srid>4326</srid>
                <authid>EPSG:4326</authid>
                <description>WGS 84</description>
                <projectionacronym>longlat</projectionacronym>
                <ellipsoidacronym>WGS84</ellipsoidacronym>
                <geographicflag>true</geographicflag>
            </spatialrefsys>
        </destinationsrs>
        <layer_coordinate_transform_info/>
    </mapcanvas>
    <visibility-presets/>
    <layer-tree-canvas>
        <custom-order enabled="0">
            <item>{layer_id}123456</item>
        </custom-order>
    </layer-tree-canvas>
    <legend updateDrawingOrder="true">
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="{layer_id}" showFeatureCount="0">
            <filegroup open="true" hidden="false">
                <legendlayerfile isInOverview="0" layerid="{layer_id}123456" visible="1"/>
            </filegroup>
        </legendlayer>
    </legend>
    <projectlayers layercount="1">
        <maplayer minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
            <id>{layer_id}123456</id>
            <datasource>dbname="{db_name}" host="{db_host}" port="{db_port}" user="{db_user}" password="{db_password}" key='ogc_fid' type={geom_type} table="({sql_select})" ({geom_field}) sql=</datasource>
            <title></title>
            <abstract></abstract>
            <keywordList>
                <value></value>
            </keywordList>
            <layername>{layer_id}</layername>
            <srs>
                <spatialrefsys>
                    <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
                    <srsid>3452</srsid>
                    <srid>4326</srid>
                    <authid>EPSG:4326</authid>
                    <description>WGS 84</description>
                    <projectionacronym>longlat</projectionacronym>
                    <ellipsoidacronym>WGS84</ellipsoidacronym>
                    <geographicflag>true</geographicflag>
                </spatialrefsys>
            </srs>
            <provider encoding="System">postgres</provider>
            <previewExpression></previewExpression>
            <vectorjoins/>
            <expressionfields/>
            <edittypes/>
            <renderer-v2 symbollevels="0" type="singleSymbol">
                <symbols>
{symbol_block}
                </symbols>
                <rotation/>
                <sizescale scalemethod="area"/>
            </renderer-v2>
            <customproperties/>
            <blendMode>0</blendMode>
            <featureBlendMode>0</featureBlendMode>
            <layerTransparency>0</layerTransparency>
            <displayfield>ogc_fid</displayfield>
            <label>0</label>
            <labelattributes>
                <label fieldname="" text="Label"/>
                <family fieldname="" name="Ubuntu"/>
                <size fieldname="" units="pt" value="12"/>
                <bold fieldname="" on="0"/>
                <italic fieldname="" on="0"/>
                <underline fieldname="" on="0"/>
                <strikeout fieldname="" on="0"/>
                <color fieldname="" red="0" blue="0" green="0"/>
                <x fieldname=""/>
                <y fieldname=""/>
                <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
                <angle fieldname="" value="0" auto="0"/>
                <alignment fieldname="" value="center"/>
                <buffercolor fieldname="" red="255" blue="255" green="255"/>
                <buffersize fieldname="" units="pt" value="1"/>
                <bufferenabled fieldname="" on=""/>
                <multilineenabled fieldname="" on=""/>
                <selectedonly on=""/>
            </labelattributes>
            <editform></editform>
            <editforminit></editforminit>
            <featformsuppress>0</featformsuppress>
            <annotationform></annotationform>
            <editorlayout>generatedlayout</editorlayout>
            <excludeAttributesWMS/>
            <excludeAttributesWFS/>
            <attributeactions/>
            <edittypes>
                <edittype widgetv2type="TextEdit" name="ogc_fid">
                    <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
                </edittype>
                <edittype widgetv2type="TextEdit" name="region">
                    <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
                </edittype>
            </edittypes>
        </maplayer>
    </projectlayers>
    <properties>
        <SpatialRefSys>
            <ProjectCRSProj4String type="QString">+proj=longlat +datum=WGS84 +no_defs</ProjectCRSProj4String>
            <ProjectCrs type="QString">EPSG:4326</ProjectCrs>
            <ProjectCRSID type="int">3452</ProjectCRSID>
        </SpatialRefSys>
        <Paths>
            <Absolute type="bool">false</Absolute>
        </Paths>
        <Gui>
            <SelectionColorBluePart type="int">0</SelectionColorBluePart>
            <CanvasColorGreenPart type="int">255</CanvasColorGreenPart>
            <CanvasColorRedPart type="int">255</CanvasColorRedPart>
            <SelectionColorRedPart type="int">255</SelectionColorRedPart>
            <SelectionColorAlphaPart type="int">255</SelectionColorAlphaPart>
            <SelectionColorGreenPart type="int">255</SelectionColorGreenPart>
            <CanvasColorBluePart type="int">255</CanvasColorBluePart>
        </Gui>
        <Digitizing>
            <LayerSnappingList type="QStringList">
                <value>{layer_id}123456</value>
            </LayerSnappingList>
            <LayerSnappingEnabledList type="QStringList">
                <value>enabled</value>
            </LayerSnappingEnabledList>
            <AvoidIntersectionsList type="QStringList"/>
            <LayerSnappingToleranceUnitList type="QStringList">
                <value>0</value>
            </LayerSnappingToleranceUnitList>
            <LayerSnapToList type="QStringList">
                <value>to_vertex</value>
            </LayerSnapToList>
            <LayerSnappingToleranceList type="QStringList">
                <value>0.000000</value>
            </LayerSnappingToleranceList>
        </Digitizing>
        <PositionPrecision>
            <DecimalPlaces type="int">2</DecimalPlaces>
            <Automatic type="bool">true</Automatic>
        </PositionPrecision>
        <Legend>
            <filterByMap type="bool">false</filterByMap>
        </Legend>
    </properties>
</qgis>"""

QGIS_SYMBOL_POINT = """                    <symbol alpha="1" type="marker" name="0">
                        <layer pass="0" class="SimpleMarker" locked="0">
                            <prop k="angle" v="0"/>
                            <prop k="color" v="156,153,246,255"/>
                            <prop k="horizontal_anchor_point" v="1"/>
                            <prop k="name" v="circle"/>
                            <prop k="offset" v="0,0"/>
                            <prop k="offset_map_unit_scale" v="0,0"/>
                            <prop k="offset_unit" v="MM"/>
                            <prop k="outline_color" v="0,0,0,255"/>
                            <prop k="outline_style" v="solid"/>
                            <prop k="outline_width" v="0"/>
                            <prop k="outline_width_map_unit_scale" v="0,0"/>
                            <prop k="outline_width_unit" v="MM"/>
                            <prop k="scale_method" v="area"/>
                            <prop k="size" v="2"/>
                            <prop k="size_map_unit_scale" v="0,0"/>
                            <prop k="size_unit" v="MM"/>
                            <prop k="vertical_anchor_point" v="1"/>
                        </layer>
                    </symbol>
"""

QGIS_SYMBOL_LINE = """                    <symbol alpha="1" type="line" name="0">
                        <layer pass="0" class="SimpleLine" locked="0">
                            <prop k="capstyle" v="square"/>
                            <prop k="customdash" v="5;2"/>
                            <prop k="customdash_map_unit_scale" v="0,0"/>
                            <prop k="customdash_unit" v="MM"/>
                            <prop k="draw_inside_polygon" v="0"/>
                            <prop k="joinstyle" v="bevel"/>
                            <prop k="line_color" v="73,130,82,255"/>
                            <prop k="line_style" v="solid"/>
                            <prop k="line_width" v="0.26"/>
                            <prop k="line_width_unit" v="MM"/>
                            <prop k="offset" v="0"/>
                            <prop k="offset_map_unit_scale" v="0,0"/>
                            <prop k="offset_unit" v="MM"/>
                            <prop k="use_custom_dash" v="0"/>
                            <prop k="width_map_unit_scale" v="0,0"/>
                        </layer>
                    </symbol>
"""

QGIS_SYMBOL_FILL = """                    <symbol alpha="1" type="fill" name="0">
                        <layer pass="0" class="SimpleFill" locked="0">
                            <prop k="border_width_map_unit_scale" v="0,0"/>
                            <prop k="color" v="98,49,189,255"/>
                            <prop k="joinstyle" v="bevel"/>
                            <prop k="offset" v="0,0"/>
                            <prop k="offset_map_unit_scale" v="0,0"/>
                            <prop k="offset_unit" v="MM"/>
                            <prop k="outline_color" v="0,0,0,255"/>
                            <prop k="outline_style" v="solid"/>
                            <prop k="outline_width" v="0.26"/>
                            <prop k="outline_width_unit" v="MM"/>
                            <prop k="style" v="solid"/>
                        </layer>
                    </symbol>
"""

QGIS_GEOMETRY_QUERY = 'SELECT GeometryType(a.{geom_field}) FROM ({sql_select}) AS a LIMIT 1'



def qgis_escape(string):
    result = string.replace('\\', '\\\\')
    result = string.replace('"', '\\"')
    return result


def qgis_generate(sql_query, layer_id, geom_field=None):
    context = {}
    if geom_field:
        context['geom_field'] = geom_field
    else:
        if 'geom' in sql_query.field_names:
            context['geom_field'] = 'geom'
        elif 'the_geom' in sql_query.field_names:
            context['geom_field'] = 'the_geom'
        else:
            raise Exception('No geometry data in the result set')

    context['sql_select'] = qgis_escape(sql_query.sql)
    geom_query = QGIS_GEOMETRY_QUERY.format(**context)
    context['geom_type'] = sql_query.conn.session.execute(geom_query).fetchone()[0]
    if context['geom_type'] == 'POLYGON':
        context['symbol_block'] = QGIS_SYMBOL_FILL
    elif context['geom_type'] == 'LINESTRING':
        context['symbol_block'] = QGIS_SYMBOL_LINE
    elif context['geom_type'] == 'POINT':
        context['symbol_block'] = QGIS_SYMBOL_POINT
    else:
        raise Exception('Could not determine geometry data type')
    
    context['layer_id'] = layer_id
    context['db_host'] = sql_query.conn.metadata._bind.url.host
    context['db_name'] = sql_query.conn.metadata._bind.url.database
    context['db_port'] = sql_query.conn.metadata._bind.url.port
    if not context['db_port']:
        context['db_port'] = '5432'
    context['db_user'] = sql_query.conn.metadata._bind.url.username
    context['db_password'] = sql_query.conn.metadata._bind.url.password

    return QGIS_TEMPLATE.format(**context)
    
