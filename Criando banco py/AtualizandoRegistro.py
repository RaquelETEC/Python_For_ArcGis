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
fields = ['NU_ID', 'NU_COMBO', "OBJECTID"]


var = 0; 
with arcpy.da.UpdateCursor(y, fields) as cursor:
        for row in cursor:
            # Verifique se o valor no campo 'NU_ID' corresponde ao valor de pesquisa
            if row[0] == 6:
                # Atualize os campos com os novos valores
                row[1] = 1  #NU_COMBO
                cursor.updateRow(row)
                
                var = var + 1

if var > 0: 
        print(str(var) + " Registros atualizados")
else:
            print("Registro não atualizado")


def AtualizarIDRegistros():
     
    var = 1; 

    with arcpy.da.UpdateCursor(y, fields) as cursor:
        for row in cursor:
                row[0] = var
                cursor.updateRow(row)
                
                var += 1

    print("Registros atualizados com sucesso")
