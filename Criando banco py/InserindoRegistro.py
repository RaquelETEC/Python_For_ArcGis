import arcpy
import os


out_path = "C:/output"  #Caminho da Pasta do banco de dados 
out_name = "fGDB.gdb"  #Caminho pra o nome do banco de dados 

geodatabase  = os.path.join(out_path, out_name)

tabela = "TB_PARAMETROS"
y = os.path.join(geodatabase , tabela)


fields = ['NU_ID', 'NU_COMBO']

with arcpy.da.InsertCursor(y,fields) as cursor:
    cursor.insertRow([1,2])
print ("Inserido com sucesso")

