import arcpy 

#caminho 
arcpy.env.workspace = 'C:/Users/MURALIS 0023/Desktop/Trabalho/Desafios/0004/DESAFIO004/DESAFIO004.gdb'
feature_class = 'Mun_Brasileiros'
fields = ["ID", "DESCRICAO", "STATUS"]

#so par exibir dados
with arcpy.da.SearchCursor(feature_class, fields) as cursor:
    for row in cursor:
        print(row)

print("------------------------------")

#abrir edição
edit = arcpy.da.Editor(arcpy.env.workspace)

# A sessão de edição é iniciada sem uma pilha de desfazer/refazer para dados versionados
# (para segundo argumento, use False para dados não versionados)
edit.startEditing(False, False)

#Start an edit operation 
edit.startOperation()

where = "OBJECTID = 5550  "

with arcpy.da.UpdateCursor(feature_class, fields, where_clause=where) as cursor:
    for row in cursor:
        row[1] = "Cidade da Raquel2"
        cursor.updateRow(row)


#fechar edicao
# Stop the edit operation.
edit.stopOperation()

# Stop the edit session and save the changes
edit.stopEditing(save_changes=True)

