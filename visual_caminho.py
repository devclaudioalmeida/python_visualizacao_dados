import matplotlib.pyplot as plt

from caminho_randomico import CaminhoRandomico

while True:
    # Gera um caminho randômico
    cr = CaminhoRandomico()
    cr.fill_walk()

    # Plota os pontos no passeio
    plt.style.use('classic')
    fig, ax = plt.subplots()
    numero_pontos = range(cr.num_pontos)
    ax.scatter(cr.valores_x, cr.valores_y, c=numero_pontos, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.set_aspect('equal')

    # Destaca o primeiro e o ultimo ponto
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(cr.valores_x[-1], cr.valores_y[-1], c='red', edgecolors='none', s=100)

    #Remove os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)   
    
    plt.show()

    # Se escolher 'n' para de gerar caminha aleatórios
    continua = input('Gerar outro caminho [s / n]? ').strip().lower()
    if continua == 'n':
        break


