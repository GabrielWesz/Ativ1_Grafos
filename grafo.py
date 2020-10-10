import sys

class Grafo:
    def __init__(self, file, n_vertices=0, n_arestas=0):
        self.file = file
        self.n_vertices = n_vertices
        self.n_arestas = n_arestas
        self.v = list()
        self.adj_matrix = list()
        self.adj_list = list()

    def le_grafo(self):
        """
        Implementa a funcionalidade de leitura de um grafo
        Abre o arquivo file, contido pelo grafo que chamou este metodo
        """
        arq = open(self.file, 'r')
        linha1 = arq.readline().split()
        self.n_vertices = int(linha1[1])
        for i in range(0, self.n_vertices):
            l = arq.readline().split()

            # Inicia a matriz de adjacencia
            self.v.append(' '.join(l[1:]))
            vector = [sys.maxsize] * self.n_vertices
            self.adj_matrix.append(vector)

            # Inicia a lista de adjacencia
            self.adj_list.append(list())



        arq.readline()  # Serve para pular a linha em que esta escrito '*edges'
        aresta = dict()
        for l in arq:
            linha = l.split()
            v1 = int(linha[0])
            v2 = int(linha[1])
            peso = linha[2]

            # Popula a matriz de adjacencia
            self.adj_matrix[v1 - 1][v2 - 1] = int(peso)

            # Popula a lista de adjacencia com a aresta e o peso
            aresta["vertice"] = v2
            aresta["peso"] = linha[2]
            self.adj_list[v1 - 1].append(aresta.copy())
            aresta.clear()
            self.n_arestas += 1

    def peso(self, u, v):
        """
        Retorna o peso de uma aresta do grafo
        """
        return self.adj_matrix[u-1][v-1]

    def ha_arestas(self, u, v):
        """
        Confere se existe aresta entre u e v
        """
        return (self.adj_matrix[u-1][v-1] != None) or (self.adj_matrix[u-1][v-1] != None)

    def vizinhos(self, v):
        """
        Retorna os vizinhos do vertice v
        """
        return self.adj_list[v-1]

    def rotulo(self, v):
        """
        Retorna o rotulo do vertice v
        """
        return self.v[v-1]

    def grau(self, v):
        """
        Retorna o grau do vertice v
        """
        return len(self.adj_list[v-1])

    def qnt_arestas(self):
        """
        Retorna a quantidade de arestas do grafo
        """
        return self.n_arestas

    def qnt_vertices(self):
        """
        Retorna a quantidade de vertices do grafo
        """
        return self.n_vertices
