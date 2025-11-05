from operator import itemgetter

import requests


# Cria a chamada de API e verifica a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Codigo do status: {r.status_code}')

# Processa as informações sobra cada contribuição de artigo
id_envios = r.json()
dict_envios = []
for id_envio in id_envios[:5]:
    # Cria uma nova chamada de API para cada contribuição do artigo
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json'.format(id_envio)
    r = requests.get(url)
    print(f'id: {id_envio}\tstatus: {r.status_code}')
    dic_resposta = r.json()

    # Cria um dicionário para cada artigo
    dict_envio = {
        'titulo' : dic_resposta['title'],
        'hn_link' : f'https://news.ycombinator.com/item?id={id_envio}',
        'comentarios' : dic_resposta['descendants'],
    }
    dict_envios.append(dict_envio)

dict_envios = sorted(dict_envios, key=itemgetter('comentarios'), reverse=True)

for dict_envio in dict_envios:
    print(f'\nTitulo: {dict_envio['titulo']}')
    print(f'Link de discussão: {dict_envio['hn_link']}')
    print(f'Comentários: {dict_envio['comentarios']}')