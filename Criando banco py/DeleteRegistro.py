import arcpy
import os

out_path = "C:/output"
out_name = "fGDB.gdb"

tabela = "TB_PARAMETROS"

geodatabase = os.path.join(out_path, out_name)

y = os.path.join(geodatabase, tabela)

where_clause = "NU_COMBO = 1"


# Crie um cursor de atualização
with arcpy.da.UpdateCursor(y, ['NU_ID'], where_clause) as cursor:
    for row in cursor:
        cursor.deleteRow()

print("Registros excluídos com sucesso.")


try:
    arcpy.DeleteRows_management(y, where_clause)
    print("Registros excluídos com sucesso.")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))  #salva o erro
except Exception as e:
    print(str(e))  # Imprime o erro