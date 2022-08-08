import json
import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
# print(url)

try:
    cot = requests.get(url)
# print(cot.status_code)
except Exception as e:
    print(f"requisição deu erro: {e}")

if cot.status_code == 200:
    print(f"Sucesso na solicitação, retornou o código {cot.status_code}, Reason {cot.reason}")
    # cot_data = cot.json()
    cot_data = json.loads(cot.content)
    dol_max = cot_data["USDBRL"]["high"]
    print(f"Moeda: {cot_data['USDBRL']['code']}, Valor: R$ {cot_data['USDBRL']['bid']}")
    dict_USDBRL = cot_data["USDBRL"].copy()
    for chave, valor in dict_USDBRL.items():
        print(f"Chave: {chave}, valor: {valor}")
else:
    print(f"Erro na solicitação, retornou o código {cot.status_code}, Reason {cot.reason}")

url = " https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

try:
  resposta = requests.get(url)
except Exception as e:
  print(f"Erro: {e}")
  exit(0)

if resposta.status_code == 200:
  dict_resposta = json.loads(resposta.text)
  # print(dict_resposta)
  # for chave in dict_resposta.keys():
  #   print(f"Chave: {chave}")
  # for valor in dict_resposta.values():
  #   print(f"Valor: {valor}")
  dict_variacao = {}
  for chave, valor in dict_resposta.items():
    print(f"A moeda {dict_resposta.get(chave).get('name').split('/')[0]}, está variando nesse momento: {dict_resposta.get(chave).get('pctChange')}%, em relação ao {dict_resposta.get(chave).get('name').split('/')[1]}")
    dict_variacao.update({chave: dict_resposta.get(chave).get('pctChange')})
else:
  print(f"Erro: {resposta.reason}, Código: {resposta.status_code}")


try:
  resposta = requests.post(url, data=json.dumps(dict_variacao))
except Exception as e:
  print(f"Erro: {e}")
  exit(0)