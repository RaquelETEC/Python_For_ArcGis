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
fields = ['NU_ID']

var = 1; 

with arcpy.da.UpdateCursor(y, fields) as cursor:
    for row in cursor:
            row[0] = var
            cursor.updateRow(row)
            
            var += 1

print("Registros atualizados com sucesso")
