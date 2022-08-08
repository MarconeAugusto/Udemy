"""
https://putsreq.com/
"""
import json

import requests

url = "https://putsreq.com/OtScQ3hikt1q81IFa5op"

# Se a conexão exigir tokem ele deve ser enviado no header
cabecalho = {"User-agent": "Ubuntu",
             "Referer": "https://google.com"}

cookies = {"Ultima-visita": "10/08/2021"}

# Códigos esperados nas requisições
# 200 ... 299 - sucesso
# 400 ... 499 - erro cliente
# 500 ... 599 - erro servidor

new_data = None

try:
    req = requests.get(url, headers=cabecalho, cookies=cookies)
    if req.status_code == 200:
        print(f"Code: {req.status_code}, Reason: {req.reason}")
        data = json.loads(req.content)
        # data = req.text
        print(data)
        for key in data.keys():
            print(f"Chave: {key}, Dado: {data.get(key)}")
            if data.get(key) == "29":
                data[key] = "30"
                new_data = data
except Exception as e:
    print(f"Erro: {e}")

try:
    # Utiliza json.dumps() para gerar um JSON de um dicionário em python
    print(json.dumps(new_data, indent=4))
    req = requests.post(url, headers=cabecalho, cookies=cookies, data=json.dumps(new_data, indent=4))
    if req.status_code == 200:
        print(f"Code: {req.status_code}, Reason: {req.reason}")
        data = json.loads(req.content)
        # data = req.text
        print(data)
except Exception as e:
    print(f"Erro: {e}")
