from grafo import Grafo

#file = input("Digite nome do arquivo: ")
g1 = Grafo("fln_pequena.net")
g1.le_grafo()
print(g1.qnt_arestas())
print(g1.qnt_vertices())
print(g1.v)
print(" ")
print("Primeiro vertice")
print(g1.v_list[0])
print(" ")
print("Segundo vertice")
print(g1.v_list[1])


