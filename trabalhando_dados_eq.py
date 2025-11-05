from pathlib import Path
import json

import plotly.express as px

# Lê os dados como uma string e os converte em objeto Python
caminho = Path('eq_data/eq_data_30_day_m1.geojson')
conteudo = caminho.read_text()
todos_dados_eq = json.loads(conteudo)

# Examina os terremotos no conjunto de dados
todos_eq_dicts = todos_dados_eq['features']
#print(len(todos_eq_dicts))
mags, lons, lats = [], [], []
for eq_dict in todos_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Exibe a fatia da lista com as 10 primeiras magnitudes 
#print(mags[:10])
# Exime as fatias com as 5 primeiras logitudes e latitudes
#print(lons[:5])
#print(lats[:5])

# Mapa Mundi

titulo = 'Terrmotos Globais'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=titulo)
fig.show()