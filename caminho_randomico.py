from random import choice

class CaminhoRandomico:
    """ Classe para gerar passeios aleatórios """
    def __init__(self, num_pontos=5000):
        """ Inicaliza os atributos de um passeio """
        self.num_pontos = num_pontos
        # Todos os passeios començam em (0,0)
        self.valores_x = [0]
        self.valores_y = [0]

    
    def get_passo(self):
        """ Calcula a direção e a distância do passo """
        direcao = choice([-1, 1])
        distancia = choice([0, 1, 2, 3, 4, 5])
        return direcao * distancia

        

    def fill_walk(self):
        """ Calcula todos os pontos do passeio """
        # Continua dando passos até que o passeio atinja o comprimento desejado

        while len(self.valores_x) < self.num_pontos:
            
            # Decisão da direção e distância do passo
            passo_x = self.get_passo()
            passo_y = self.get_passo()

            # Ignora passos que não vão a lugar nenhum
            if passo_x == 0 and passo_y == 0:
                continue

            # Calcula a nova posição
            x = self.valores_x[-1] + passo_x
            y = self.valores_y[-1] + passo_y

            self.valores_x.append(x)
            self.valores_y.append(y)

