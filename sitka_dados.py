from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('dados_meteorologia/sitka_weather_2021_simple.csv')
linhas = path.read_text().splitlines()

leitor = csv.reader(linhas)
linha_cabecalho = next(leitor)
#for index, column_header in enumerate(linha_cabecalho):
#    print(index, column_header)

datas, maximas, minimas = [], [], []
for linha in leitor:
    data = datetime.strptime(linha[2], '%Y-%m-%d')
    maxima = int(linha[4])
    minima = int(linha[5])
    maximas.append(maxima)
    datas.append(data)
    minimas.append(minima)

# Plota as temperaturas mínimas e máximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(datas, maximas, color='red', alpha=0.5) # Plota as máximas em vermelho
ax.plot(datas, minimas, color='blue', alpha=0.5) # Plota as mínimas em azul
ax.fill_between(datas, maximas, minimas, facecolor='blue', alpha=0.1 ) # Faz uma sobra na area entre as máximas e mínimas

# Formata o gráfico
ax.set_title('Temperaturas mínimas e máximas registradas em 2021', fontsize=22)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperaturas (F)º', fontsize=16)
ax.tick_params(labelsize=16)

# Mostra o gráfico na tela
plt.show()