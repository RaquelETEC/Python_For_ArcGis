import arcpy
import os
import datetime

# Caminhos dos bancos de dados
bd01_path = "C:/output/BD01.gdb"
bd02_path = "C:/output/BD02.gdb"

# Tabelas de origem e destino
CaminhoFuncionarios = os.path.join(bd01_path, 'FUNCIONARIOS')
CaminhoFuncionarios_Fab = os.path.join(bd02_path, 'FUNCIONARIOS_FABRICA')

# Campos a serem copiados
fields = ['ID', 'NOME', 'RG', 'CPF', 'DATA_ADMISSAO', 'DATA_HORA_ALTERACAO_DO_REGISTRO']

# Atualize a tabela de destino com base no campo ID
with arcpy.da.UpdateCursor(CaminhoFuncionarios_Fab, fields) as destino_cursor:
    for destino_row in destino_cursor:
        # Obtenha o valor do campo ID da tabela de destino
        id_destino = destino_row[0]

        SQLWHERE = arcpy.AddFieldDelimiters(CaminhoFuncionarios, "ID") + " = {}".format(id_destino)

        with arcpy.da.SearchCursor(CaminhoFuncionarios, fields, where_clause=SQLWHERE) as origem_cursor:
            for origem_row in origem_cursor:
              
                for i in range(len(fields)):
                    destino_row[i] = origem_row[i]

                destino_row[-1] = datetime.datetime.now()
                #Atualizando
                destino_cursor.updateRow(destino_row)

print("Funcionários atualizados com sucesso.")