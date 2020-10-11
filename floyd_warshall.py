import sys

from grafo import Grafo


class Warshall:
    def __init__(self, arquivo_grafo):
        """
        Recebe um grafo ja lido pelo metodo g1.legrafo()
        """
        self.g1 = arquivo_grafo
        self.matriz_adj = self.g1.adj_matrix
        self.n_vertices = self.g1.qnt_vertices()

    def floyd_warshall(self):
        # Inicia a matriz distancia com os mesmo valores da matriz de adjacencia.
        # A menor distancia entre nodos vizinhos eh o peso das suas transicoes.
        matriz_dist = self.matriz_adj.copy()

        # Vertice intermediario que sera usado para comparar distancias.
        # e.g.  origem = 1, destino = 4, inter = 2
        # 1 ---> 2 ---> 4
        for inter in range(self.n_vertices):

            # Vertice i e o vertice origem
            for i in range(self.n_vertices):

                # Vertice j e o vertice destino
                for j in range(self.n_vertices):
                    matriz_dist[i][j] = min(matriz_dist[i][j], matriz_dist[i][inter] + matriz_dist[inter][j])

        return matriz_dist
