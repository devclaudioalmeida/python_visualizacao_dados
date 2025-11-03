import plotly.express as px

from dado import Dado

#Instancia de dois dados
d1 = Dado() #Dado com 6 lados
d2 = Dado() #Dado com 6 lados
d3 = Dado() #Dado com 6 lados

#lista para armazenar os resultados
resultados = []

#Faz muitas jogas dos dados e armazena os resultados
#for jogada in range(1_001):
#    resultado = d1.jogar_dado() + d2.jogar_dado() +d3.jogar_dado()
#    resultados.append(resultado)
  
resultados = [(d1.jogar_dado() + d2.jogar_dado() + d3.jogar_dado()) for jog in range(1_001)] # Usando List Comprehensions

# Analisa os resultados
frequencias = []
result_possiveis = range(3, (d1.lados + d2.lados + d3.lados + 1))
frequencias = [resultados.count(valor) for valor in result_possiveis] # Usando List Comprehensions

#for valor in result_possiveis:
    #frequencias.append(resultados.count(valor))

# Vizualização em gráficos
titulo = 'Resultados de 1.000 jogadas de dois dados D8'
rotulos = {'x' : 'Resultados', 'y': 'Frequencia do resultado'}
fig = px.bar(x=result_possiveis, y=frequencias, title=titulo, labels=rotulos)
#fig = px.pie(values= frequencias, names=result_possiveis)

# Personaliza ainda mais o gráfico
fig.update_layout(xaxis_dtick=1)

fig.show()
