import arcpy
import os
import datetime

out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "BD01.gdb"  #Caminho pra o nome do banco de dados 

geodatabase  = os.path.join(out_path, out_name)

if(not arcpy.Exists(geodatabase)):
    arcpy.CreateFileGDB_management(out_path, out_name )

#Criando Tabelas 
CaminhoClientes  = os.path.join(geodatabase , 'CLIENTES')

#Verifica se Tabela não existe
if(not arcpy.Exists(CaminhoClientes)):
      arcpy.management.CreateTable(geodatabase , 'CLIENTES', out_alias="Clientes")

#CriandosColunasfuncionarios
arcpy.management.AddField(CaminhoClientes, "ID", "short", field_alias="ID", )
arcpy.management.AddField(CaminhoClientes, "NOME", "Text", field_alias="Nome", )
arcpy.management.AddField(CaminhoClientes, "RG", "Text", field_alias="Rg", )
arcpy.management.AddField(CaminhoClientes, "CPF", "Text", field_alias="Cpf", )
arcpy.management.AddField(CaminhoClientes, "LATITUDE", "Double", field_alias="Latitude")
arcpy.management.AddField(CaminhoClientes, "LONGITUDE", "Double", field_alias="Longitude")
arcpy.management.AddField(CaminhoClientes, "DATA_ADMISSAO", "Date", field_alias="Data Admissão", )
arcpy.management.AddField(CaminhoClientes, "DATA_HORA_ALTERACAO_DO_REGISTRO", "Date", field_alias="Alteração do Registro", )

print ("Tabela Cliente Criada Com Sucesso")


#Populando tabela Funcionarios com pelo menos 10 registros completos.
fields = ['ID', 'NOME','RG', 'CPF','Latitude','Longitude', 'DATA_ADMISSAO','DATA_HORA_ALTERACAO_DO_REGISTRO']
with arcpy.da.InsertCursor(CaminhoClientes,fields) as cursor:
    cursor.insertRow([1,'Jaqueline',2910408,26234280981,-23.56149777192690,-46.37845376971240,datetime.datetime(2023,10,25),datetime.datetime(2023,10,25,14,50)])
    cursor.insertRow([2,'beatriz',4488995,13573716926,-23.541135959247400,-46.456881383100500,datetime.datetime(2023,10,20),datetime.datetime(2023,10,25,14,59)])
    cursor.insertRow([3,'paul',3317079,19395236891,-23.52240533485770,-46.34321618559550,datetime.datetime(2022,11,15),datetime.datetime(2023,10,25,15,10)])
    cursor.insertRow([4,'Janaina',7227835,40104766277,-23.547197441076600,-46.216380104095300,datetime.datetime(2021,9,10),datetime.datetime(2023,10,25,15,15)])
    cursor.insertRow([5,'Rita',4882090,63954058800,-23.55066547461630,-46.199413506814600,datetime.datetime(2003,7,15),datetime.datetime(2023,10,25,15,30)])
    cursor.insertRow([6,'Roberto',2594815,16169012632,-23.50319579417060,-46.510557283784900,datetime.datetime(2021,3,1),datetime.datetime(2023,10,25,15,15)])
    cursor.insertRow([7,'Carlos',2966827,80870846117,-23.53588668505950,-46.526492127766200,datetime.datetime(2021,10,9),datetime.datetime(2023,10,25,16,30)])
    cursor.insertRow([8,'Samuel',2749171,92564406028,-23.493695453647600,-46.6259532129608,datetime.datetime(2022,10,8),datetime.datetime(2023,10,25,17,13)])
    cursor.insertRow([9,'Alice',4987361,38151798376,-23.58767596130320,-46.68295639812720,datetime.datetime(2023,10,7),datetime.datetime(2023,10,25,18,11)])
    cursor.insertRow([10,'Elizabeth',4141515,65861564025,-23.701474538767300,-46.54779487543030,datetime.datetime(2015,10,12),datetime.datetime(2023,10,25,10,4)])
print ("Inseridos com sucesso")



