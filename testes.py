from grafo import Grafo
from busca_largura import Busca
from ciclo_euleriano import Ciclo
import output_exercicios
from bellman_ford import Bellman


g1 = Grafo("bford")
g1.le_grafo()

"""
print("Lista de adjacencia:\n")
print(g1.adj_list)

print("\nMatriz de Adjacencia:\n")
print(g1.adj_matrix)

#print(len(g1.adj_matrix))
#print(" ")
print(g1.peso(1,8))
print(g1.grau(2))
print(g1.grau(1))
print(g1.ha_arestas(1, 8))
print(g1.rotulo(3))
b_largura = Busca(g1, 1)
list_dist = b_largura.alg_busca()

output_exercicios.exercicio2(list_dist)
b_largura = Busca(g1, 1)

list_dist = b_largura.alg_busca()

output_exercicios.exercicio2(list_dist)
"""
ex4 = Bellman(g1)
print(ex4.bellman_ford(1))