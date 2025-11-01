import matplotlib.pyplot as plt


def plota_grafico(pontos):
    """Função simples para plotar um gráfico de função quadrática na tela"""

    # Gera a lista de pontos para o gráfico
    valores_x = range(0, pontos+1)
    valores_y = []
    for x in valores_x:
        y = (x ** 2)
        valores_y.append(y)

    # Estiliza o gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    #ax.scatter(2, 5) #Plota um único ponto passando as coodenadas de x e y;
    ax.scatter(valores_x, valores_y, c=valores_y, cmap=plt.cm.Purples, s=10)
    #ax.plot(valores_x, valores_y, color=(0, 0.8, 0), linewidth=3) #Plota o gráfico em linha contínua
    # Define o título do gráfico e os rótulos dos eixos
    str = f'Função com os {pontos} primeiros quadrados'
    ax.set_title(str, fontsize=18)
    ax.set_xlabel('Valores', fontsize=12)
    ax.set_ylabel('Quadrados dos valores', fontsize=12)
    # Define o tamano dos rótulos de marcação de escala
    ax.tick_params(labelsize=14)
    ax.axis([0, max(valores_x), 0, max(valores_y)])# Define o intervalo para cada eixo
    ax.ticklabel_format(style='plain') #Modifica a notação da marcação de escala para notação
    # Exibe o gráfico na tela
    plt.show()


plota_grafico(100)