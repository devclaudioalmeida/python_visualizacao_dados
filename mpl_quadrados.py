import matplotlib.pyplot as plt

def plota_grafico(pontos):
    """Função simples para plotar um gráfico de função quadrática na tela"""

    # Gera a lista de pontos para o gráfico
    quadrados = []
    for i in range (1, pontos+1):
        n = i ** 2
        quadrados.append(n)

    fig, ax = plt.subplots()
    ax.plot(quadrados, linewidth=3)
    # Define o título do gráfico e os rótulos dos eixos
    str = f'Função com os {pontos} primeiros quadrados'
    ax.set_title(str, fontsize=18)
    ax.set_xlabel('Valores', fontsize=12)
    ax.set_ylabel('Quadrados dos valores', fontsize=12)
    # Define o tamano dos rótulos de marcação de escala
    ax.tick_params(labelsize=14)
    # Exibe o gráfico na tela
    plt.show()


plota_grafico(100)