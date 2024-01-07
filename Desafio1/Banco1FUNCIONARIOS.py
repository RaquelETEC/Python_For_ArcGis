import arcpy
import os
import datetime


out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "BD01.gdb"  #Caminho pra o nome do banco de dados 


geodatabase  = os.path.join(out_path, out_name)


if(not arcpy.Exists(geodatabase)):
    arcpy.CreateFileGDB_management(out_path, out_name )


#Criando Tabelas 
CaminhoFuncionarios = os.path.join(geodatabase , 'FUNCIONARIOS')

#Verifica se Tabela não existe
if(not arcpy.Exists(CaminhoFuncionarios)):
      arcpy.management.CreateTable(geodatabase , 'FUNCIONARIOS', out_alias="funcionarios")

# #CriandosColunasfuncionarios
# arcpy.management.AddField(CaminhoFuncionarios, "ID", "short", field_alias="ID", )
# arcpy.management.AddField(CaminhoFuncionarios, "NOME", "Text", field_alias="Nome", )
# arcpy.management.AddField(CaminhoFuncionarios, "RG", "Text", field_alias="Rg", )
# arcpy.management.AddField(CaminhoFuncionarios, "CPF", "Text", field_alias="Cpf", )
# arcpy.management.AddField(CaminhoFuncionarios, "LATITUDE", "Double", field_alias="Latitude")
# arcpy.management.AddField(CaminhoFuncionarios, "LONGITUDE", "Double", field_alias="Longitude")
# arcpy.management.AddField(CaminhoFuncionarios, "DATA_ADMISSAO", "Date", field_alias="Data Admissão", )
# arcpy.management.AddField(CaminhoFuncionarios, "DATA_HORA_ALTERACAO_DO_REGISTRO", "Date", field_alias="Alteração do Registro", )

#print ("Tabela Funcionario Criada Com Sucesso")


#Populando tabela Funcionarios com pelo menos 10 registros completos.
fields = ['ID', 'NOME','RG', 'CPF','Latitude','Longitude', 'DATA_ADMISSAO','DATA_HORA_ALTERACAO_DO_REGISTRO']
with arcpy.da.InsertCursor(CaminhoFuncionarios,fields) as cursor:
    cursor.insertRow([1,'Raquel Silva','3981506183','41983129852',-23.5224649842631,-46.18611597707990,datetime.datetime(2023,10,25),datetime.datetime(2023,10,25,14,50)])
    cursor.insertRow([2,'Ivan João Dominato','36489015','65239875',-23.52505063610920,-46.169442327612500,datetime.datetime(2023,10,20),datetime.datetime(2023,10,25,14,59)])
    cursor.insertRow([3,'Emanuel Feliciano','56971309','123456789',-23.524824707390600,-46.18641714316230,datetime.datetime(2022,11,15),datetime.datetime(2023,10,25,15,10)])
    cursor.insertRow([4,'Altino Heron Bonilha Neto','48480328','123456789',-23.52552945267840,-46.19142008697580,datetime.datetime(2021,9,10),datetime.datetime(2023,10,25,15,15)])
    cursor.insertRow([5,'Dante Denis de Camacho Sobrinho','781541489','123456789',-23.525559476563100,-46.1653873123736,datetime.datetime(2003,7,15),datetime.datetime(2023,10,25,15,30)])
    cursor.insertRow([6,'Jean Martin Carrara Ortega','12342684','123456789',-23.519854815514400,-46.17773241429180,datetime.datetime(2021,3,1),datetime.datetime(2023,10,25,15,15)])
    cursor.insertRow([7,'Joaquin Camacho Castelo','9871515','123456789',-23.51805329224460,-46.19593898412280,datetime.datetime(2021,10,9),datetime.datetime(2023,10,25,16,30)])
    cursor.insertRow([8,'Meire Soraya Bonilha','6528815151','123456789',-23.534528835104600,-46.31749739564980,datetime.datetime(2022,10,8),datetime.datetime(2023,10,25,17,13)])
    cursor.insertRow([9,'Kelly Colaço Rossi','7849269125','123456789',-23.493620730366700,-46.37707037746380,datetime.datetime(2023,10,7),datetime.datetime(2023,10,25,18,11)])
    cursor.insertRow([10,'Benjamin Corona','9858151818','123456789',-23.442777513480400,-46.330087002242500,datetime.datetime(2015,10,12),datetime.datetime(2023,10,25,10,4)])
print ("Inseridos com sucesso")



