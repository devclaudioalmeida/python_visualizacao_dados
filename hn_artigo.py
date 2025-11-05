import requests
import json

# Cria a chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
r = requests.get(url)
print(f'Codigo do Status: {r.status_code}')

# Explora a estrutura dos dados
dict_resposta = r.json()
string_resposta = json.dumps(dict_resposta, indent=4)
print(string_resposta)