import arcpy
import os

#Criando variaveis para os caminhos das pastas 
out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "fGDB.gdb"  #Caminho pra o nome do banco de dados 

#Concatenando na variavel x o caminho do banco e o nome do banco 
geodatabase  = os.path.join(out_path, out_name)

#Fazendo uma validação para ver se não existe o arquivo do banco ja criado, se não , crie
if(not arcpy.Exists(geodatabase)):
    arcpy.CreateFileGDB_management(out_path, out_name )

#Criando Tabelas 
tabela = "TB_PARAMETROS"

y = os.path.join(geodatabase , tabela)
if(not arcpy.Exists(y)):
    arcpy.management.CreateTable(geodatabase , tabela, out_alias="PARAMETROS")


# #Criando domonio
dominio = "DO_STATUS2"
# # arcpy.management.CreateDomain(geodatabase , dominio, "Selecoinar Status", "short", "CODED", "default", "default")
# arcpy.management.CreateDomain(geodatabase , dominio)

# #Criando opções
# domDict = { 1:"Ativo",
#             2:"Inativo",
#             3:"Desativado"
#            }

# for code in domDict:        
#     arcpy.management.AddCodedValueToDomain(geodatabase, dominio, code, domDict[code])


#CRIANDO OS CAMPOS DA TABELA
arcpy.management.AddField(y, "NU_ID", "short", field_alias="ID", )
arcpy.management.AddField(y, "NU_COMBO", "short", field_alias="ID", field_domain= dominio)


# Open a search cursor on a feature class / table to read from









#So um teste para aprender como chama uma função
'''

def funcao(teste="Raquel"):
    print(teste)

funcao()
funcao("TESTE")
'''