from grafo import Grafo
from queue import Queue


class Ciclo:

    def __init__(self, arq_grafo):
        """
        Recebe um grafo já lido pelo método grafo.le_grafo()
        Cria lista para indicar se uma aresta já foi visitada (list_visitado)
        Cria lista de vértices para indicar o ciclo do grafo (list_ciclo)
        """
        self.g1 = arq_grafo
        self.list_visitado = list()
        self.list_ciclo = list()

        """
        Popula a list_visitado, que possuem tamanho igual ao número
        de arestas do grafo
        Obs: a list_ciclo não precisa ser populada agora
        """
        for a in range(0, Grafo.qnt_arestas(self.g1)):
            self.list_visitado.append(False)

    """
    Implementa o algoritmo de Hierholzer, descrito na página 35 das anotações da disciplina
    Esse algoritmo invoca um algoritmo auxiliar, o alg_subciclo()
    
    """
    def alg_hierholzer(self):
        pass

    """
    Implementa o algoritmo auxiliar de busca de subciclos eulerianos, descrito na página 36 das anotações
    É invocado pela função alg_hierholzer()
    """
    def alg_subciclo(self):
        pass
