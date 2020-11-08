from grafo import Grafo

class Kruskal:

    def __init__(self, arq_grafo):
        self.g1 = arq_grafo
        self.lista_adj = self.g1.adj_list
        self.lista_arestas = self.g1.arestas



    def arvore_minima(self):
        A = list()
        S = list()

        for i in range(self.g1.qnt_vertices()):
            S.append([i])

        arestas_ordenadas = sorted(self.lista_arestas, key=lambda k: k['peso'])

        for aresta in arestas_ordenadas:
            v1 = aresta['v_origem'] - 1
            v2 = aresta['v_destino'] - 1

            S_v1 = S[v1].copy()
            S_v1.sort()
            S_v2 = S[v2].copy()
            S_v2.sort()
            if S_v1 != S_v2:
                A.append([v1, v2])
                X = list()
                X.append(S[v1] + S[v2])

                for v in X[0]:
                    for e in X[0]:
                        S[v].append(e)
                        S[v] = list(dict.fromkeys(S[v]))

        return A, S

