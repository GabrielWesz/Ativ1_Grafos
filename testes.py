from grafo import Grafo
from busca_largura import Busca
from ciclo_euleriano import Ciclo
import output_exercicios
from bellman_ford import Bellman
from floyd_warshall import Warshall

arq = input("Digite o nome do arquivo: ")
g1 = Grafo(arq)
g1.le_grafo()

ex2 = Busca(g1, 1)
ex3 = Ciclo(g1)
ex4 = Bellman(g1)
ex5 = Warshall(g1)

out_ex5 = ex5.floyd_warshall()
output_exercicios.exercicio5(out_ex5)
