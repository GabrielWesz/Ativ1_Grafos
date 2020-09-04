from grafo import Grafo

#file = input("Digite nome do arquivo: ")
g1 = Grafo("fln_pequena.net")
g1.le_grafo()

#print(len(g1.adj_matrix))
#print(" ")
print(g1.peso(1,8))

print(g1.grau(2))
print(g1.grau(1))

print(g1.ha_arestas(1, 8))

print(g1.rotulo(3))

print(g1.vizinhos(2))
