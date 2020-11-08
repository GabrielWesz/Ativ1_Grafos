from grafo import Grafo
from busca_largura import Busca
from ciclo_euleriano import Ciclo
import output_exercicios
from bellman_ford import Bellman
from floyd_warshall import Warshall
from conexos import Conexos
from ordenacao_topologica import Ordenacao
from kruskal import Kruskal

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

"""-----------------------------------------------------------------------------------------------------------------"""
print('Atividade 2\nGabriel Wesz e Matheus Eyng')
ex6 = Conexos(g1)
ex7 = Ordenacao(g1)
ex8 = Kruskal(g1)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exercício 1: ')
out_ex6 = ex6.cacula_conexos()
output_exercicios.exercicio6(out_ex6)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exercício 2: ')
out_ex7 = ex7.ordenacao_topologica()
output_exercicios.exercicio7(out_ex7)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exercício 3: ')
out_ex81, out_ex82 = ex8.arvore_minima()
output_exercicios.exercicio8(out_ex81, out_ex82)