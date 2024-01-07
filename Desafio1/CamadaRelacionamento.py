import arcpy
import os

# Defina o caminho para o projeto do ArcGIS Pro projeto = arcpy.mp.ArcGISProject("C:/Users/MURALIS 0023/Desktop/Trabalho/Python/Desafio1/Projeto.aprx")


out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "BD01.gdb"  #Caminho pra o nome do banco de dados 

geodatabase  = os.path.join(out_path, out_name)

SQL ="""
SELECT 
FUNCIONARIOS.NOME, 
FUNCIONARIOS.RG,
FUNCIONARIOS.CPF, 
CLIENTES.NOME, 
CLIENTES.RG,
CLIENTES.CPF
CLIENTES.LATITUDE,
CLIENTES.LONGITUDE,
ATENDIMENTO.DATA 
FROM ATENDIMENTO JOIN CLIENTES ON (ATENDIMENTO.ID_CLIENTE = CLIENTES.ID)
                 JOIN FUNCIONARIOS ON (ATENDIMENTO.ID_FUNCIONARIO = FUNCIONARIOS.ID)
"""

nome_camada = "RelacaoAtendimentos"


arcpy.management.MakeQueryLayer(geodatabase, nome_camada, SQL)

# Adicionar a camada ao mapa ativo no ArcGIS Pro
aprx = arcpy.mp.ArcGISProject("CURRENT")  # Projeto atualmente aberto no ArcGIS Pro
mapa = aprx.listMaps()[0]  # Use o primeiro mapa do projeto
mapa.addLayer(nome_camada)

# Salvar o projeto
aprx.save()

print(f"Camada {nome_camada} criada e adicionada ao mapa com sucesso.")