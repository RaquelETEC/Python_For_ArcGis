import arcpy
import os

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



def atualizar (sql, dominio): 
    try:
        # Caminho para o banco de dados original
        caminho_origem = r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0001\ForestGIS_Geodatabase.gdb'
        camada_origem = os.path.join(caminho_origem, 'BRA_MUNICIPIOS_BRASIL')

        # Caminho para o novo banco de dados
        caminho_destino = r'C:\Users\MURALIS 0023\Desktop\Trabalho\Desafios\0004\DESAFIO004\DESAFIO004.gdb'
        camada_destino = 'Mun_Brasileiros'

        query_expression = sql
        campos = ["COD_IBGE", "NOME_MUNI", "SHAPE@"]

        camada_destino_path = os.path.join(caminho_destino, camada_destino)

        insercao = InserirDadosClasss(camada_destino_path)


        with arcpy.da.SearchCursor(camada_origem, campos , where_clause = sql) as cursor:
            for row in cursor:
                cod_ibge = row[0]
                nome_muni = row[1]
                shape = row[2]
                arcpy.AddMessage('antes de insercao')
                insercao.inserir_dados(shape,cod_ibge, nome_muni, dominio )
                arcpy.AddMessage('depois de insercao')

    except NameError:
        print('ERRO' + NameError)


WHERE = "COD_UF = 31"
STATUS = 3
arcpy.AddMessage('Iniciando execução')

atualizar(WHERE,STATUS )