import sys
from grafo import Grafo


class Conexos:

    def __init__(self, arq_grafo):
        self.g1 = arq_grafo
        self.lista_adj = self.g1.adj_list
        self.lista_adj_transposta = self.g1.adj_list_transposed

    def cacula_conexos(self):
        (v_visitados, t_inicial, t_final, anterior) = self.dfs(self.lista_adj)
        (v_visitadosT, t_inicialT, t_finalT, anteriorT) = self.dfs_modificado(self.lista_adj_transposta, t_final.copy())
        self.formata_output(anteriorT)

    """
    Para avaliar os arcos de maneira decrescente, chame este metodo com o 
    argumento False
    """
    def dfs(self, lista_adj):
        qnt_vertices = Grafo.qnt_vertices(self.g1)

        v_visitados = [False] * qnt_vertices

        t_inicial = [sys.maxsize] * qnt_vertices
        t_final = [sys.maxsize] * qnt_vertices
        anterior = [None] * qnt_vertices
        tempo = [0]

        for u in range(len(self.lista_adj)):
            if not v_visitados[u]:
                self.dfs_visit(u, v_visitados, t_inicial, t_final, anterior, tempo, lista_adj)

        return v_visitados, t_inicial, t_final, anterior

    def dfs_modificado(self, lista_adj, t_final_anterior):
        qnt_vertices = Grafo.qnt_vertices(self.g1)

        v_visitados = [False] * qnt_vertices

        t_inicial = [sys.maxsize] * qnt_vertices
        t_final = [sys.maxsize] * qnt_vertices
        anterior = [None] * qnt_vertices
        tempo = [0]

        decrescente = list()

        for i in range(qnt_vertices):
            maior = 0
            indice = 0
            for j in range(qnt_vertices):
                if t_final_anterior[j] > maior:
                    maior = t_final_anterior[j]
                    indice = j

            t_final_anterior[indice] = -1
            decrescente.append(indice)


        for u in decrescente:
            if not v_visitados[u]:
                self.dfs_visit(u, v_visitados, t_inicial, t_final, anterior, tempo, lista_adj)

        return v_visitados, t_inicial, t_final, anterior

    """
    Recebe o indice do vertice de origem
    """
    def dfs_visit(self, v_origem, visitados, t_inicial, t_final, anterior, tempo, lista_adj):
        visitados[v_origem] = True
        tempo[0] = tempo[0] + 1
        t_inicial[v_origem] = tempo[0]

        for u in range(len(lista_adj[v_origem])):
            vertice = lista_adj[v_origem][u]["vertice"] - 1
            if not visitados[vertice]:
                anterior[vertice] = v_origem
                self.dfs_visit(vertice, visitados, t_inicial, t_final, anterior, tempo, lista_adj)

        tempo[0] = tempo[0] + 1
        t_final[v_origem] = tempo[0]

    def formata_output(self, anteriorT):
        raizes = list()
        for vertice in range(len(anteriorT)):
            if anteriorT[vertice] is None:
                raizes.append([vertice])

        tamanho = 0
        while tamanho < self.g1.qnt_vertices():
            for vertice in range(len(anteriorT)):
                for raiz in raizes:
                    if raiz[-1] == anteriorT[vertice]:
                        raiz.append(vertice)
            tamanho = 0
            for r in raizes:
                tamanho += len(r)

        for r in raizes:
            for v in range(len(r)):
                r[v] += 1

        for r in raizes:
            print(r)