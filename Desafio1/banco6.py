import arcpy
import os
import datetime

out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "BD01.gdb"  #Caminho pra o nome do banco de dados 

geodatabase  = os.path.join(out_path, out_name)

if(not arcpy.Exists(geodatabase)):
    arcpy.CreateFileGDB_management(out_path, out_name )

#Criando Tabelas 
CaminhoVisitas  = os.path.join(geodatabase , 'VISITAS')

#Verifica se Tabela não existe
if(not arcpy.Exists(CaminhoVisitas)):
      arcpy.management.CreateTable(geodatabase , 'VISITAS', out_alias="VISITAS")

#CriandosColunasfuncionarios
arcpy.management.AddField(CaminhoVisitas, "ID_ATENDIMENTO", "ID", field_alias="ID_ATENDIMENTO", )
arcpy.management.AddField(CaminhoVisitas, "VIS_CLIENTE", "text", field_alias="Cliente", )
arcpy.management.AddField(CaminhoVisitas, "VIS_CLIENTE_RG", "text", field_alias="Cliente RG", )
arcpy.management.AddField(CaminhoVisitas, "VIS_CLIENTE_CPF", "text", field_alias="Cliente CPF", )
arcpy.management.AddField(CaminhoVisitas, "VIS_FUNCIONARIO", "text", field_alias="Funcionario", )
arcpy.management.AddField(CaminhoVisitas, "VIS_FUNCIONARIO_RG", "text", field_alias="Funcionario RG", )
arcpy.management.AddField(CaminhoVisitas, "VIS_FUNCIONARIO_CPF", "text", field_alias="Funcionario CPF", )
arcpy.management.AddField(CaminhoVisitas, "VIS_DATA", "Date", field_alias="Data Atendimento", )

print ("Tabela VISITAS Criada Com Sucesso")


CaminhoFuncionarios = os.path.join(geodatabase, 'FUNCIONARIOS')
CaminhoClientes  = os.path.join(geodatabase , 'CLIENTES')



# Campos a serem copiados
fieldsFuncionarios = ['ID', 'NOME', 'RG', 'CPF']

# Atualize a tabela de destino com base no campo ID
with arcpy.da.UpdateCursor(CaminhoVisitas, fieldsFuncionarios) as destino_cursor:
    for destino_row in destino_cursor:
        # Obtenha o valor do campo ID da tabela de destino
        id_destino = destino_row[0]

        SQLWHERE = arcpy.AddFieldDelimiters(CaminhoFuncionarios, "ID") + " = {}".format(id_destino)

        with arcpy.da.SearchCursor(CaminhoFuncionarios, fieldsFuncionarios, where_clause=SQLWHERE) as origem_cursor:
            for origem_row in origem_cursor:
              
                for i in range(len(fieldsFuncionarios)):
                    destino_row[i] = origem_row[i]

                destino_row[-1] = datetime.datetime.now()
                #Atualizando
                destino_cursor.updateRow(
                    
                )


# Campos a serem copiados
fieldsClientes = ['ID', 'NOME', 'RG', 'CPF']

#Atualize a tabela de destino com base no campo ID
with arcpy.da.UpdateCursor(CaminhoVisitas, fieldsClientes) as destino_cursor:
    for destino_row in destino_cursor:
        # Obtenha o valor do campo ID da tabela de destino
        id_destino = destino_row[0]

        SQLWHERE = arcpy.AddFieldDelimiters(CaminhoFuncionarios, "ID") + " = {}".format(id_destino)

        with arcpy.da.SearchCursor(CaminhoFuncionarios, fieldsClientes, where_clause=SQLWHERE) as origem_cursor:
            for origem_row in origem_cursor:
              
                for i in range(len(fieldsFuncionarios)):
                    destino_row[i] = origem_row[i]

                destino_row[-1] = datetime.datetime.now()
                #Atualizando
                destino_cursor.updateRow(destino_row)



print("Funcionários atualizados com sucesso.")





print ("Inseridos com sucesso")



