import requests

# Cria uma chamada de API e verifica a resposta
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

cabecalhos = {'Accept' : 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=cabecalhos)
print(f'Código de status: {r.status_code}')

# Converte o objeto de resposta em um dicionário
resposta_dict = r.json()

# Processa os resultados
#print(resposta_dict.keys())

print(f'Total de repositórios:: {resposta_dict['total_count']}')
print(f'Resultados completos: {not resposta_dict['incomplete_results']}')

# Explora as informaçẽos sobre os resultados
repo_dicts = resposta_dict['items']
print(f'Numero de repositórios retornados {len(repo_dicts)}')

# Examina o primeiro repositório
repo_dict = repo_dicts[0]
print(f'\nChaves: {len(repo_dict)}')
for key in sorted(repo_dict.keys()):
    print(key)