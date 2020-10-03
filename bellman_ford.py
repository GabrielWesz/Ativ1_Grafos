import sys
from grafo import Grafo

class Bellman:
    def __init__(self, arq_grafo):
        """
        Recebe um grafo já lido pelo método grafo.le_grafo()
        Cria lista para indicar se uma aresta já foi visitada (list_visitado)
        Cria lista de vértices para indicar o ciclo do grafo (list_ciclo)
        """
        self.g1 = arq_grafo
        self.peso_caminho = list()
        self.lista_anterior = list()
        self.adj_list = self.g1.adj_list


    def inicializacao(self, s):
        # Inicia a lista de pesos
        # Preenche a lista de pesos com peso infinito
        self.peso_caminho = [sys.maxsize] * Grafo.qnt_vertices(self.g1)

        # Inicia a lista de vertices anteriores
        # Preenche a lista com None
        self.lista_anterior = [None] * Grafo.qnt_vertices(self.g1)

        self.peso_caminho[s - 1] = 0

    def relaxamento(self, u, v):
        peso_uv = Grafo.peso(self.g1, u, v)
        novo_peso = self.peso_caminho[u - 1] + int(peso_uv)

        if self.peso_caminho[v - 1] > novo_peso:
            self.peso_caminho[v - 1] = novo_peso
            if self.lista_anterior[v - 1] is None:
                self.lista_anterior[v - 1] = list()
            self.lista_anterior[v - 1].append(u)

    def bellman_ford(self, v_inicial):
        self.inicializacao(v_inicial)

        # Loop de 1 ate |V| - 1
        for i in range(Grafo.qnt_vertices(self.g1)):
                for j in range(len(self.adj_list[i])):
                    self.relaxamento(i + 1, self.adj_list[i][j]["vertice"])

        for v1 in range(Grafo.qnt_vertices(self.g1)):
            for v2 in range(len(self.adj_list[v1])):

                vizinhos = Grafo.vizinhos(self.g1, v1)
                if vizinhos:
                    peso_uv = Grafo.peso(self.g1, v1 + 1, self.adj_list[v1][v2]["vertice"])
                    novo_peso = self.peso_caminho[v1] + int(peso_uv)

                    if self.peso_caminho[i] > novo_peso:
                        return None

        return [True, self.peso_caminho, self.lista_anterior]

