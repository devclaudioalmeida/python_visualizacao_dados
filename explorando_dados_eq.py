from pathlib import Path
import json

path = Path('eq_data/eq_data_1_day_m1.geojson')
conteudo  = path.read_text()
todos_dados_eq = json.loads(conteudo)

# Cria uma versão mais amigável do arquivo de dados
path = Path('eq_data/legivel_eq_data.geojson')
cont_legivel = json.dumps(todos_dados_eq, indent=4)
path.write_text(cont_legivel)