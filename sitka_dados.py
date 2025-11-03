from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('dados_meteorologia/sitka_weather_07-2021_simple.csv')
linhas = path.read_text().splitlines()

leitor = csv.reader(linhas)
linha_cabecalho = next(leitor)
#for index, column_header in enumerate(linha_cabecalho):
#    print(index, column_header)

maximas = []
for linha in leitor:
    maxima = int(linha[4])
    maximas.append(maxima)

# Plota as temperaturas máximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(maximas, color='red')

# Formata o gráfico
ax.set_title('Temperaturas máximas registradas em Julho de 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperaturas (F)º', fontsize=16)
ax.tick_params(labelsize=16)

# Mostra o gráfico na tela
plt.show()