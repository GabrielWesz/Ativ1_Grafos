from grafo import Grafo
from conexos import Conexos
from kruskal import Kruskal

arq = "kruskal.txt"
g1 = Grafo(arq)
g1.le_grafo()

#conexos = Conexos(g1)
#conexos.cacula_conexos()

kruskal = Kruskal(g1)
kruskal.arvore_minima()