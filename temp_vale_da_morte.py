from pathlib import Path
import csv
from datetime import datetime

from matplotlib import pyplot as plt

path = Path('dados_meteorologia/death_valley_2021_simple.csv')
linhas = path.read_text().splitlines()

leitor = csv.reader(linhas)
linha_cabecalho = next(leitor)

datas, maximas, minimas = [], [], []
for linha in leitor:
    data = datetime.strptime(linha[2], '%Y-%m-%d')
    try:
        maxima = int(linha[3])
        minima = int(linha[4])
    except ValueError:
        print(f'Não há dados para {data}')
    else:
        datas.append(data)
        maximas.append(maxima)
        minimas.append(minima)


#Plota as temperaturas máximas e mínimas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(datas, maximas, color='red', alpha=0.8)
ax.plot(datas, minimas, color='blue', alpha=0.8)
ax.fill_between(datas, maximas, minimas, facecolor='blue', alpha=0.1)

#Formatação do gráfico
ax.set_title('Temperatures máximas e mínimas em 2021\n Vale da Morte, CA', fontsize=22)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperaturas (F)º', fontsize=16)
ax.tick_params(labelsize=14)

#Mostra o gráfico na tela
plt.show()