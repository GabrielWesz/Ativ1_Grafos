from queue import Queue


"""
Implementa funções para mostrar o output de cada exercício
de acordo com o formato pedido pela atividade
"""


def exercicio2(list_dist):
    nivel_set = set()
    vetores = list()
    ld = list_dist.copy()
    for i in range(0, len(ld)):
        if ld[i] == float('inf'):
            continue
        else:
            nivel_set.add(ld[i])
            vetores.append([ld[i], i+1])
    niveis = list(nivel_set)
    niveis.sort()
    vetores.sort()
    v_list = list()
    atual = -1
    for v in vetores:
        i = v[0]
        if atual == i:
            v_list[i].append(v[1])
        else:
            v_list.append([v[1]])
            atual += 1
    for n in niveis:
        print(f'{n}: ', end="")
        print(*v_list[n])

