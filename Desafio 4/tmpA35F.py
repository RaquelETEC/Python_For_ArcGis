# consulta e insert
# validação
# parametros de entra no PRO

import arcpy
import json
import sys 
import locale

class scriptFindPlusCode(): 


    arcpy.env.workspace = r"C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0004\DESAFIO004\DESAFIO004.gdb"
          

    def validacao(self, texto):
        """ 
            Valida se o texto esta vazio.
            Valida se o texto esta nullo.
            Valida se o texto é numérico
            Retorna True/False
        """
        if (texto == None or texto.strip == "") and texto.isnumeric(): 
            return False
        else: 
            return True

      

    def inicializar(self):
        txtwhere = arcpy.GetParameterAsText(0)
        txtwhere3 = arcpy.GetParameterValue(0)
        txtstatus = int(arcpy.GetParameterAsText(1))
        camada_origem = arcpy.GetParameter(2)
        camada_destino = arcpy.GetParameter(3)

        # txtwhere = "99"
        # txtstatus = "4"
        # camada_origem = r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0001\ForestGIS_Geodatabase.gdb\BRA_MUNICIPIOS_BRASIL'
        # camada_destino =  r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0004\DESAFIO004\DESAFIO004.gdb\Mun_Brasileiros'
       
        fields = ["COD_IBGE", "NOME_MUNI", "SHAPE@"]
        i = 0
        if self.validacao(txtwhere) == False:
            arcpy.AddMessage("UF inválida.")
        else:
            expression = "COD_UF = " + txtwhere + ""

            #abrir edição
            edit = arcpy.da.Editor(arcpy.env.workspace)
            edit.startEditing(False, False)
            #Start an edit operation 
            edit.startOperation()

            with arcpy.da.SearchCursor(camada_origem, fields, where_clause = expression) as cursor:
                for row in cursor:
                    with arcpy.da.InsertCursor(camada_destino, ["SHAPE@", "ID", "DESCRICAO", "STATUS"]) as cursor2:
                        cursor2.insertRow((row[2], row[0], row[1], txtstatus))
                        i += 1
        if (i > 0):
            arcpy.AddMessage(f"{i} Valores inseridos com sucesso na camada de destino.")
        else:
            arcpy.AddMessage("Não foi possivel achar o UF selecionado")

        # Stop the edit operation.
        edit.stopOperation()

        # Stop the edit session and save the changes
        edit.stopEditing(save_changes=False)


if __name__ == '__main__':
    main = scriptFindPlusCode()
    main.inicializar()