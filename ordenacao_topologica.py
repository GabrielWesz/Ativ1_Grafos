from grafo import Grafo


class Ordenacao:

    def __init__(self, arq_grafo):
        self.g1 = arq_grafo
        """Define listas e popula com valores iniciais"""
        self.l_visitado = list()
        self.l_tempo = list()
        self.l_volta = list()
        self.l_ordenacao = list()

        for v in range(0, Grafo.qnt_vertices(self.g1)):
            rotulo = Grafo.rotulo(self.g1, v)
            self.l_visitado.append(list((False, rotulo)))
            self.l_tempo.append(list((float("inf"), rotulo)))
            self.l_volta.append(list((float("inf"), rotulo)))

    def dfs_ot(self):
        tempo = 0

        for u in range(0, Grafo.qnt_vertices(self.g1)):
            if self.l_visitado[u][0] is False:
                self.dfs_visita_ot(u, tempo)

        return self.l_ordenacao

    def dfs_visita_ot(self, vu, temp):
        u = vu
        tempo = temp

        self.l_visitado[u][0] = True
        tempo += 1
        self.l_tempo[u][0] = tempo

        """
        Aqui vai um for -> para cada vizinho dependente de u, se 
        ainda não foi visitado, visite utilizando algoritmo 17,
        que está na página 69 da apostila
        """
        """A inserção na lista de ordenação deve ser no início da lista"""
        tempo += 1
        self.l_volta[u][0] = tempo
        self.l_ordenacao.insert(0, self.l_visitado[u][1])
