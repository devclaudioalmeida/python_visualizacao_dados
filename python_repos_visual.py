import requests
import plotly.express as px

# Cria uma chamada de API e verifica a resposta
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

cabecalhos = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url, headers=cabecalhos)
print(f'Código de Status: {r.status_code}')

#Processa os resultados gerais
dic_resposta = r.json()
print(f'Resultados completos: {not dic_resposta['incomplete_results']}')

# Processa as informações do repositório
repo_dicts = dic_resposta['items']
repo_names, estrelas = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    estrelas.append(repo_dict['stargazers_count'])

# Cria a visualização
fig = px.bar(x=repo_names, y=estrelas)
fig.show()