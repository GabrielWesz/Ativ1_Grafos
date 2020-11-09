from grafo import Grafo
from conexos import Conexos
from kruskal import Kruskal

arq = "kruskal.txt"
arq_conexos = "conexos.txt"
g1 = Grafo(arq)
g1.le_grafo()
g2 = Grafo(arq_conexos)
g2.le_grafo()

print("Teste conexos")
conexos = Conexos(g2)
conexos.cacula_conexos()

print("Teste kruskal")
kruskal = Kruskal(g1)
kruskal.arvore_minima()