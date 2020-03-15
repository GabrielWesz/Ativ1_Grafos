class Grafo:
    def __init__(self, file, n_vertices=0, n_arestas=0):
        self.file = file
        self.n_vertices = n_vertices
        self.n_arestas = n_arestas
        self.v = list()
        self.e = list()

    def le_grafo(self):
        """
        Implementa a funcionalidade de leitura de um grafo
        Abre o arquivo file, contido pelo grafo que chamou este metodo
        """
        arq = open(self.file, 'r')
        linha1 = arq.readline().split()
        vertice = dict()
        self.n_vertices = int(linha1[1])
        for i in range(0, self.n_vertices):
            l = arq.readline().split()
            vertice["Indice"] = l[0]
            vertice["Rotulo"] = ' '.join(l[1:])
            self.v.append(vertice.copy())
            vertice.clear()
        arq.readline()  # Serve para pular a linha em que está escrito '*edges'
        aresta = dict()
        for l in arq:
            linha = l.split()
            aresta["V1"] = linha[0]
            aresta["V2"] = linha[1]
            aresta["Peso"] = linha[2]
            self.e.append(aresta.copy())
            aresta.clear()
        self.n_arestas = len(self.e)

    def peso(self, u, v):
        """
        Retorna o peso de uma aresta do grafo
        """
        pass

    def ha_arestas(self, u, v):
        """
        Confere se existe aresta entre u e v
        """
        pass

    def vizinhos(self, v):
        """
        Retorna os vizinhos do vertice v
        """
        pass

    def rotulo(self, v):
        """
        Retorna o rotulo do vertice v
        """
        pass

    def grau(self, v):
        """
        Retorna o grau do vertice v
        """
        pass

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
