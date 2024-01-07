import arcpy
import os
import datetime

out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "BD01.gdb"  #Caminho pra o nome do banco de dados 

geodatabase  = os.path.join(out_path, out_name)

if(not arcpy.Exists(geodatabase)):
    arcpy.CreateFileGDB_management(out_path, out_name )

#Criando Tabelas 
CaminhoClientes  = os.path.join(geodatabase , 'ATENDIMENTO')

#Verifica se Tabela não existe
if(not arcpy.Exists(CaminhoClientes)):
      arcpy.management.CreateTable(geodatabase , 'ATENDIMENTO', out_alias="ATENDIMENTO")

#CriandosColunasfuncionarios
arcpy.management.AddField(CaminhoClientes, "ID", "short", field_alias="ID", )
arcpy.management.AddField(CaminhoClientes, "ID_CLIENTE", "short", field_alias="Cliente", )
arcpy.management.AddField(CaminhoClientes, "ID_FUNCIONARIO", "short", field_alias="Funcionario", )
arcpy.management.AddField(CaminhoClientes, "DATA", "Date", field_alias="Data Atendimento", )

print ("Tabela Cliente Criada Com Sucesso")


#Populando tabela Funcionarios com pelo menos 10 registros completos.
fields = ['ID', 'ID_CLIENTE','ID_FUNCIONARIO' ,'DATA']
with arcpy.da.InsertCursor(CaminhoClientes,fields) as cursor:
    cursor.insertRow([1,1,2, datetime.datetime(2023,7, 13)])
    cursor.insertRow([2,1,3, datetime.datetime(2023,8, 6)])
    cursor.insertRow([3,4,1, datetime.datetime(2023,9, 5)])
    cursor.insertRow([4,9,4, datetime.datetime(2023,10, 12)])
    cursor.insertRow([5,2,5, datetime.datetime(2023,11, 25)])
    cursor.insertRow([6,3,6, datetime.datetime(2023,12, 18)])
    cursor.insertRow([7,5,7, datetime.datetime(2022,1, 7)])
    cursor.insertRow([8,6,8, datetime.datetime(2022,2, 14)])
    cursor.insertRow([9,7,9, datetime.datetime(2022,3, 22)])
    cursor.insertRow([10,8,10, datetime.datetime(2023,4, 30)])
    cursor.insertRow([11,2,1, datetime.datetime(2023,5, 15)])
    cursor.insertRow([12,3,2, datetime.datetime(2023,6, 8)])
    cursor.insertRow([13,4,3, datetime.datetime(2022,7, 23)])
    cursor.insertRow([14,5,4, datetime.datetime(2022,8, 10)])
    cursor.insertRow([15,6,5, datetime.datetime(2023,9, 27)])
    cursor.insertRow([16,7,6, datetime.datetime(2022,10, 14)])
    cursor.insertRow([17,8,7, datetime.datetime(2022,11, 2)])
    cursor.insertRow([18,9,8, datetime.datetime(2022,12, 19)])
    cursor.insertRow([19,10,9, datetime.datetime(2022,1, 31)])
    cursor.insertRow([20,10,10, datetime.datetime(2021,2, 16)])

print ("Inseridos com sucesso")



