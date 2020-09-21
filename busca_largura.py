from grafo import Grafo
from queue import Queue


class Busca:

    def __init__(self, arq_grafo, index_origem):
        """
        Recebe um grafo já lido pelo método grafo.le_grafo()
        Também recebe o índice de um vértice, que será a origem da busca em largura
        """
        self.g1 = arq_grafo
        self.v_origem = index_origem
        self.list_visitado = list()
        self.list_distancia = list()
        self.list_antecessor = list()
        """
        Popula as listas, elas têm tamanho igual ao número de vértices do grafo
        list_visitado -> indica se o vértice correspondente foi visitado na busca
        list_distancia -> indica a distância (em número de arestas) entre origem e o vértice
        list_antecessor -> indica qual o vértice antecessor do vértice correspondente
        Por padrão, o vértice de origem já foi visitado, tem distância zero e não possui antecessor
        """
        for v in range(0, Grafo.qnt_vertices(self.g1)):
            if self.v_origem-1 == v:
                self.list_visitado.append(True)
                self.list_distancia.append(0)
                self.list_antecessor.append(None)
            else:
                self.list_visitado.append(False)
                self.list_distancia.append(float("inf"))
                self.list_antecessor.append(None)

    def alg_busca(self):
        # Instância a fila e enfileira a origem
        q = Queue(0)
        q.put(self.v_origem)

        while not q.empty():
            # Desenfileira o próximo vertice e busca a lista de seus vizinhos
            v_atual = q.get()
            list_vizinho = Grafo.vizinhos(self.g1, v_atual)

            # Para cada vizinho do vértice atual
            for v in list_vizinho:
                """
                Se vizinho v ainda não foi visitado, então visite-o
                Setamos o vizinho como visitado
                A distância dele até a origem é a dist do antecessor +1
                O antecessor do vizinho v é o v_atual
                Enfileiramos o vizinho
                """
                index = v["vertice"]
                if not self.list_visitado[index-1]:
                    self.list_visitado[index-1] = True
                    self.list_distancia[index-1] = self.list_distancia[v_atual-1] + 1
                    self.list_antecessor[index-1] = v_atual
                    q.put(v["vertice"])

        """
        No retorno, caso seja necessário, podemos retornar também a lista de antecessores
        """
        return self.list_distancia
