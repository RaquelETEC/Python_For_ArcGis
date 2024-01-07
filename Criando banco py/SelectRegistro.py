import arcpy
import os

out_path = "C:/output"
out_name = "fGDB.gdb"

tabela = "TB_PARAMETROS"

# banco de dados 
geodatabase = os.path.join(out_path, out_name)

# Caminho completo para a tabela
y = os.path.join(geodatabase, tabela)

#atualizar  campos 
fields = ['NU_ID', 'NU_COMBO', "OBJECTID"]

# sql_clause_py = (None, "SELECT NU_ID, " +
#                         "CASE WHEN NU_COMBO = 1 THEN 'Ativo' " +
#                         "WHEN NU_COMBO = 2 THEN 'Inativo' " +
#                         "WHEN NU_COMBO = 3 THEN 'Desativado' " +
#                         "ELSE 'Outro' END AS NU_COMBO, OBJECTID " +
#                  "FROM TB_PARAMETROS")



# Crie um cursor de pesquisa
with arcpy.da.SearchCursor(y, fields,  where_clause='NU_COMBO = 3',  sql_clause=(None, 'ORDER BY OBJECTID desc' )) as cursor:
    for row in cursor:
        # Imprima os valores dos campos para cada registro
        nu_id = row[0]
        nu_combo = row[1]
        objectid = row[2]
        print(f'NU_ID: {nu_id}, NU_COMBO: {nu_combo}, ID_ArcGis: {objectid} ')

