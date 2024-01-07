import requests

url = "https://sigel.aneel.gov.br/arcgis/rest/services/IMAGEM/ValidadorDUPLTV6/GPServer/uploads/upload"

payload = {'f': 'pJSON'}

files=[
  ('file',('Mem_Descritivo_LT__440kV_ARQ2_ARQ_TESTE.zip',open(r'C:/Users/MURALIS 0023/Desktop/Trabalho/Python/APIS/Mem_Descritivo_LT__440kV_ARQ2_ARQ_TESTE.zip','rb'),'application/zip'))
]
headers = {
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
