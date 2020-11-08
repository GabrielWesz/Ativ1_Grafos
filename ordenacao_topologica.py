from grafo import Grafo
import sys


class Ordenacao:

    def __init__(self, arq_grafo):
        self.g1 = arq_grafo
        self.nv = Grafo.qnt_vertices(self.g1)
        self.lista_adj = self.g1.adj_list

    def ordenacao_topologica(self):
        v_visitado = [False] * self.nv
        ordenado = []

        for v in range(0, self.nv):
            if v_visitado[v] is False:
                self.visita(v, v_visitado, ordenado)

        for i in range(len(ordenado)):
            aux = ordenado[i]
            ordenado[i] = Grafo.rotulo(self.g1, aux+1)
        return ordenado

    def visita(self, v_atual, v_visitado, ordenado):
        v_visitado[v_atual] = True

        for i in range(len(self.lista_adj[v_atual])):
            v = self.lista_adj[v_atual][i]["vertice"]-1
            if v_visitado[v] is False:
                self.visita(v, v_visitado, ordenado)

        ordenado.insert(0, v_atual)
