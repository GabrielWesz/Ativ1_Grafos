from grafo import Grafo
from busca_largura import Busca
import output_exercicios
from ciclo_euler import Ciclo

file = input("Digite nome do arquivo: ")
g1 = Grafo(file)
g1.le_grafo()

"""
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
"""
c = Ciclo(g1)
r, ciclo = c.alg_hierholzer()
print(f'{int(r)}\n{ciclo}')
