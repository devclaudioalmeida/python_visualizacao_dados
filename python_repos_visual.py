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
repo_links, estrelas, hover_textos = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    estrelas.append(repo_dict['stargazers_count'])

    # Cria textos flutuantes
    proprietario = repo_dict['owner']['login']
    descricao = repo_dict['description']
    hover_texto = f'{proprietario} <br /> {descricao}'
    hover_textos.append(hover_texto)

# Cria a visualização
titulo = 'Projetos Python com mais estrelas no GitHub'
rotulos = {'x': 'Reposittório', 'y' : 'Estrelas'}
fig = px.bar(x=repo_links, y=estrelas, title=titulo, labels=rotulos, hover_name=hover_textos)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()