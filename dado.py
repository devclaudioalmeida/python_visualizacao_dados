from random import randint

class Dado:
    """ Classe para representar um dado de seis lados """
    def __init__(self, num_lados=6):
        """ Inicializa os atributos do dado """
        self.lados = num_lados

    def jogar_dado(self):
        """ Faz uma jogada do dado retornando o resultado """
        return randint(1, self.lados)