from grafo import Grafo
from queue import Queue


class Ciclo:

    def __init__(self, arq_grafo, index_origem):
        """
        Recebe um grafo já lido pelo método grafo.le_grafo()
        Cria lista para indicar se uma aresta já foi visitada (list_visitado)
        Cria lista de vértices para indicar o ciclo do grafo (list_ciclo)
        """
        self.g1 = arq_grafo
        self.list_visitado = list()
        self.list_ciclo = list()
        self.lista_vertices = self.g1.adj_list
        self.index_origem = index_origem

        """
        Popula a list_visitado, que possuem tamanho igual ao número
        de arestas do grafo
        Obs: a list_ciclo não precisa ser populada agora
        """

        for v in range(len(self.lista_vertices)):
            self.list_visitado.append(list())
            for e in range(len(self.lista_vertices[v])):
                self.list_visitado[v].append(False)

    """
    Implementa o algoritmo de Hierholzer, descrito na página 35 das anotações da disciplina
    Esse algoritmo invoca um algoritmo auxiliar, o alg_subciclo()

    """

    def alg_hierholzer(self):

        ciclo = self.alg_subciclo(self.index_origem)
        if ciclo == None:
            return None
        else:
            for v in self.list_visitado:
                if False in v:
                    return None
            self.list_ciclo.append(ciclo)
            return ciclo

    """
    Implementa o algoritmo auxiliar de busca de subciclos eulerianos, descrito na página 36 das anotações
    É invocado pela função alg_hierholzer()
    """

    def alg_subciclo(self, v_atual):
        ciclo = list()
        ciclo.append(v_atual)
        t = v_atual
        t_equals_v = False

        while not t_equals_v:

            if not False in self.list_visitado[v_atual-1]:
                return None
            else:
                u = 0
                while self.list_visitado[v_atual-1][u] != False:
                    u = u + 1
                else:
                    vertice = self.lista_vertices[v_atual-1][u]["vertice"]
                    self.list_visitado[v_atual-1][u] = True
                    v_atual = vertice
                    ciclo.append(vertice)
            t_equals_v = t == v_atual

        for vertice in range(len(self.list_visitado)):
            for e in range(len(self.list_visitado[vertice])):
                if self.list_visitado[vertice][e] == False:
                    subciclo = self.alg_subciclo(self.lista_vertices[vertice][e]["vertice"])
                    if subciclo == None:
                        return None
                    ciclo = self.adiciona_subciclo(ciclo, subciclo)
        return ciclo

    def adiciona_subciclo(self, ciclo, subciclo):
        return 0
    