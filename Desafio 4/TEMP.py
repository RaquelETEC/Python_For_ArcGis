# consulta e insert
# validação
# parametros de entra no PRO

import arcpy
import json
import sys 
import locale

class scriptFindPlusCode(): 

    def validacao(self, texto):
        """ 
            Valida se o texto esta vazio.
            Valida se o texto esta nullo.

            Retorna True/False
        """
        if (texto == None or texto.strip == "") and texto.isnumeric(): 
            return False
        else: 
            return True

      

    def inicializar(self):
        txtwhere = "99" #str(arcpy.GetParameterAsText(0))
        # txtstatus = int(arcpy.GetParameterAsText(1))
        # camada_origem = arcpy.GetParameter(2)
        # camada_destino = arcpy.GetParameter(3)

        #txtwhere = "asdf__"


        txtstatus = '3'
        camada_origem = r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0001\ForestGIS_Geodatabase.gdb\BRA_MUNICIPIOS_BRASIL'
        camada_destino =  r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0004\DESAFIO004\DESAFIO004.gdb\Mun_Brasileiros'

        fields = ["COD_IBGE", "NOME_MUNI", "SHAPE@"]
        
        inseriu = False
        if self.validacao(txtwhere) == False:
            arcpy.AddMessage("UF inválida.")
            #pass
        else:
            expression = "UF = '" + txtwhere + "'"
            with arcpy.da.SearchCursor(camada_origem, fields, where_clause = expression) as cursor:
                for row in cursor:
                    with arcpy.da.InsertCursor(camada_destino, ["SHAPE@", "ID", "DESCRICAO", "STATUS"]) as cursor:
                        cursor.insertRow((row[2], row[0], row[1], txtstatus))
                        inseriu = True

                if inseriu == True: 
                    arcpy.AddMessage("Valores inseridos com sucesso na camada de destino.")
                else:
                    arcpy.AddMessage("Não foi localizada UF selecionada, escolha outra")


if __name__ == '__main__':
    main = scriptFindPlusCode()
    main.inicializar()