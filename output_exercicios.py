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


def exercicio3(ciclo):
    if ciclo is None:
        print(f'0\n"Nenhum caminho euleriano possivel"')
    else:
        print(1)
        print(*ciclo, sep=", ")


def exercicio4(matrix):
    if matrix is None:
        print('Erro')
    else:
        peso = list()
        peso.extend(matrix[1])
        vert = list()
        vert.extend(matrix[2])
        for v in range(len(vert)):
            if vert[v] is not None:
                print(f'{v}: ', end="")
                print(*vert[v], sep=',', end="")
                print(f' d={peso[v]}')
            else:
                print(f'{v}: {v}; d={peso[v]}')


def exercicio5(matrix):
    for i in range(len(matrix)):
        print(f'{i+1}: ', end="")
        for p in matrix[i]:
            if p > 10000000000:
                print(f'{0},', end="")
            else:
                print(f'{p},', end='')
        print()

def exercicio6(i):
    for j in i:
        print(f'{j}, ',end='')
    print()

def exercicio7(l_ordenada):
    for i in range(len(l_ordenada)):
        print(f'{l_ordenada[i]} -> ', end='')
    print()


def exercicio8(duplas, soma):
    v = 0
    for s in soma:
        v += sum(s)
    print(v)
    for i in duplas:
        print(f'{i} ',end='')
    print()
