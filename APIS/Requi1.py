import requests
import json 

url = "https://sigel.aneel.gov.br/arcgis/rest/services/IMAGEM/ValidadorDUPLTV6/GPServer/uploads/upload"

arquivo_zip = "Mem_Descritivo_LT__440kV_ARQ2_ARQ_TESTE.zip"
com_arquivo = open(arquivo_zip,"rb")

conteudo_binario = com_arquivo.read()

params = {
    "file":conteudo_binario,
    "f": "JSON"
}
headers = {"Content-Type": "application/octet-stream"}

resposta = requests.post(url, headers=headers, data=params )

if resposta.status_code == 200:
    print("Requisição bem-sucedida")
else:
    print("Requisição falhou")

com_arquivo.close()