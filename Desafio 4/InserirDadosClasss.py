import arcpy

class InserirDadosClasss():


    def __init__(self,caminho_destino):
        try:
                arcpy.AddMessage('Iniciando execução - construtor')
                self.caminho_destino = caminho_destino

        except NameError:
            print('ERRO' + NameError)

    def inserir_dados(self,shape,cod_ibge, nome_muni, dominio ):
        arcpy.AddMessage('Iniciando inserir dados ')
        try:
            with arcpy.da.InsertCursor(self.caminho_destino, ["SHAPE@", "ID", "DESCRICAO", "STATUS"]) as insert_cursor:
                insert_cursor.insertRow((shape, cod_ibge, nome_muni, dominio))
                del insert_cursor

            arcpy.AddMessage("Valores inseridos com sucesso na camada de destino.")
        except Exception as e:
            arcpy.AddError("Erro ao inserir dados: {}".format(str(e)))