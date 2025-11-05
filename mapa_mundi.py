from pathlib import Path
import json

import plotly.express as px

caminho = Path('eq_data/eq_data_30_day_m1.geojson')
conteudo = caminho.read_text()

todos_dados = json.loads(conteudo)

todos_eq_dicts = todos_dados['features']

lats, lons, mags, eq_titles= [], [], [], []
for eq_dict in todos_eq_dicts:

    lats.append(eq_dict['geometry']['coordinates'][1])
    lons.append(eq_dict['geometry']['coordinates'][0])
    mags.append(eq_dict['properties']['mag'])
    eq_titles.append(eq_dict['properties']['title'])

# Configurando a plotagem do mapa
titulo = todos_dados['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=titulo,
        color=mags, color_continuous_scale='hot',
        labels={'color' : 'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )

fig.show()
