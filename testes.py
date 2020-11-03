from grafo import Grafo
from busca_largura import Busca
from ciclo_euleriano import Ciclo
import output_exercicios
from bellman_ford import Bellman
from floyd_warshall import Warshall
from ordenacao_topologica import Ordenacao

arq = input("Digite o nome do arquivo: ")
g1 = Grafo(arq)
g1.le_grafo()

"""
ex2 = Busca(g1, 1)
ex3 = Ciclo(g1)
ex4 = Bellman(g1)
ex5 = Warshall(g1)

print('Exercício 2: ')
out_ex2 = ex2.alg_busca()
output_exercicios.exercicio2(out_ex2)
print("----------------------------")

print('Exercício 3: ')
out_ex3 = ex3.ciclo_euleriano()
output_exercicios.exercicio3(out_ex3)
print("----------------------------")

print('Exercício 4: ')
out_ex4 = ex4.bellman_ford(1)
output_exercicios.exercicio4(out_ex4)
print("----------------------------")

print('Exercício 5: ')
out_ex5 = ex5.floyd_warshall()
output_exercicios.exercicio5(out_ex5)
"""

ex7 = Ordenacao(g1)
retorno = ex7.dfs_ot()
print(retorno)
