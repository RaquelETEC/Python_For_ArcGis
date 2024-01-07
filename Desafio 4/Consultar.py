import arcpy
import os

geodatabase_path = r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0001\ForestGIS_Geodatabase.gdb'

CaminhoBRA_MUNICIPIOS_BRASIL= os.path.join(geodatabase_path, 'BRA_MUNICIPIOS_BRASIL')

layer_name = 'BRA_MUNICIPIOS_BRASIL'

query_expression = "COD_UF = 35 "

arcpy.env.workspace = geodatabase_path

campos = ["COD_IBGE", "NOME_MUNI", "Shape@"]

#arcpy.MakeFeatureLayer_management(layer_name, CaminhoBRA_MUNICIPIOS_BRASIL, query_expression)

print('COD_IBGE , NOME_MUNI , Shape, STATUS')  
with arcpy.da.SearchCursor(CaminhoBRA_MUNICIPIOS_BRASIL, campos, query_expression) as cursor:
    for row in cursor:
        cod_ibge = row[0]
        nome_muni = row[1]
        Shape = row[2]
        print(f"{cod_ibge}, {nome_muni}, {Shape} A")
 
