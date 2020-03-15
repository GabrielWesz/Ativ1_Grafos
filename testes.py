from grafo import Grafo

file = input("Digite nome do arquivo: ")
g1 = Grafo(file)
g1.le_grafo()
print(g1.qnt_arestas())
print(g1.qnt_vertices())

