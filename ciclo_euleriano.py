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
        self.lista_vertices = self.g1.adj_list


    def caminho_euleriano(self):

        pilha_vertices = [1]

        caminho = list()

        while pilha_vertices:
            vertice_atual = pilha_vertices[-1]

            if self.lista_vertices[vertice_atual - 1]:
                proximo_vertice = self.lista_vertices[vertice_atual - 1][0]["vertice"]
                del self.lista_vertices[vertice_atual - 1][0]

                pilha_vertices.append(proximo_vertice)

            else:
                caminho.append(pilha_vertices.pop())

        return caminho


    def ciclo_euleriano(self):
        ciclo = self.caminho_euleriano()
        if ciclo[0] == ciclo[-1]:
            return ciclo
        else:
            return "Nenhum caminho euleriano possivel"
    