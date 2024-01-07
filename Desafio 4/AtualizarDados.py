import arcpy
import os

# Caminho para o banco de dados original
geodatabase_path_original = r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0001\ForestGIS_Geodatabase.gdb'
CaminhoBRA_MUNICIPIOS_BRASIL = os.path.join(geodatabase_path_original, 'BRA_MUNICIPIOS_BRASIL')

# Caminho para o novo banco de dados
geodatabase_path_novo = r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0004\DESAFIO004\DESAFIO004.gdb'
camada_destino = 'Mun_Brasileiros'

query_expression = "COD_UF <> 35"
campos = ["COD_IBGE", "NOME_MUNI", "SHAPE@"]

valores_a_inserir = []

with arcpy.da.SearchCursor(CaminhoBRA_MUNICIPIOS_BRASIL, campos, query_expression) as cursor:
    for row in cursor:
        cod_ibge = row[0]
        nome_muni = row[1]
        shape = row[2]
        valores_a_inserir.append((shape, cod_ibge, nome_muni, 2))  #

camada_destino_path = os.path.join(geodatabase_path_novo, camada_destino)

with arcpy.da.InsertCursor(camada_destino_path, ["SHAPE@", "ID", "DESCRICAO", "STATUS"]) as cursor:
    for valor in valores_a_inserir:
        cursor.insertRow(valor)

print("Valores inseridos com sucesso na camada de destino.")





