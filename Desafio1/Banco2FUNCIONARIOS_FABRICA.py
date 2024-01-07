import arcpy
import os
import datetime

out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "BD02.gdb"  #Caminho pra o nome do banco de dados 

geodatabase  = os.path.join(out_path, out_name)

if(not arcpy.Exists(geodatabase)):
    arcpy.CreateFileGDB_management(out_path, out_name )

#Criando Tabelas 
CaminhoFuncionarios_Fab = os.path.join(geodatabase , 'FUNCIONARIOS_FABRICA')

#Verifica se Tabela não existe
if(not arcpy.Exists(CaminhoFuncionarios_Fab)):
      arcpy.management.CreateTable(geodatabase , 'FUNCIONARIOS_FABRICA', out_alias="funcionarios fabrica")

#CriandosColunasCaminhoFuncionarios_Fab
arcpy.management.AddField(CaminhoFuncionarios_Fab, "ID", "short", field_alias="ID", )
arcpy.management.AddField(CaminhoFuncionarios_Fab, "NOME", "Text", field_alias="Nome", )
arcpy.management.AddField(CaminhoFuncionarios_Fab, "RG", "Text", field_alias="Rg", )
arcpy.management.AddField(CaminhoFuncionarios_Fab, "CPF", "Text", field_alias="Cpf", )
arcpy.management.AddField(CaminhoFuncionarios_Fab, "DATA_ADMISSAO", "Date", field_alias="Data Admissão", )
arcpy.management.AddField(CaminhoFuncionarios_Fab, "DATA_HORA_ALTERACAO_DO_REGISTRO", "Date", field_alias="Alteração do Registro", )
print ("Tabela Funcionarios_Fab Criada Com Sucesso")

#Populando tabela Funcionarios Fabrica com pelo menos 10 registros, somente com ID e nome
fields = ['ID', 'NOME','RG', 'CPF','DATA_ADMISSAO','DATA_HORA_ALTERACAO_DO_REGISTRO']
with arcpy.da.InsertCursor(CaminhoFuncionarios_Fab, fields) as cursor:
    cursor.insertRow([1, 'Raquel Silva', None, None, None, None])
    cursor.insertRow([2, 'Ivan João Dominato', None, None, None, None])
    cursor.insertRow([3, 'Emanuel Feliciano', None, None, None, None])
    cursor.insertRow([4, 'Altino Heron Bonilha Neto', None, None, None, None])
    cursor.insertRow([5, 'Dante Denis de Camacho Sobrinho', None, None, None, None])
    cursor.insertRow([6, 'Jean Martin Carrara Ortega', None, None, None, None])
    cursor.insertRow([7, 'Joaquin Camacho Castelo', None, None, None, None])
    cursor.insertRow([8, 'Meire Soraya Bonilha', None, None, None, None])
    cursor.insertRow([9, 'Kelly Colaço Rossi', None, None, None, None])
    cursor.insertRow([10, 'Benjamin Corona', None, None, None, None])
print ("Inseridos com sucesso")



