from grafo import Grafo


class Ciclo:

    def __init__(self, arq_grafo):
        """
        Recebe um grafo já lido pelo método grafo.le_grafo()
        Cria lista para indicar se uma aresta já foi visitada (aresta_visitada)
        Cria lista de vértices para indicar o ciclo do grafo (ciclo)
        Cria variável index_origem, que receberá o vértice inicial do ciclo
        """

        self.g1 = arq_grafo
        self.ciclo = list()
        self.aresta_visitada = list()
        self.index_origem = None

        """
        Popula a list_visitado, que possuem tamanho igual ao número
        de arestas do grafo e cada elemento é uma lista com três elementos:
        0- Vértice de origem da aresta
        1- Vértice de destino da aresta
        2- Booleano que indica se aresta foi visitada (percorrida)
        Obs: a list_ciclo não precisa ser populada agora
        """

        for v in range(len(self.g1.adj_list)):
            for e in range(len(self.g1.adj_list[v])):
                self.aresta_visitada.append([v+1, self.g1.adj_list[v][e]["vertice"], False])

    """
    Implementa o algoritmo de Hierholzer, descrito na página 35 das anotações da disciplina
    Esse algoritmo invoca um algoritmo auxiliar, o alg_subciclo()
    """
    def alg_hierholzer(self):

        r, ciclo = self.alg_subciclo(1)

        if r is False:
            return False, None
        else:
            for a in self.aresta_visitada:
                if a[2] is False:
                    return False, None
            return True, ciclo


    """
    Implementa o algoritmo auxiliar de busca de subciclos eulerianos, descrito na página 36 das anotações
    É invocado pela função alg_hierholzer()
    """
    def alg_subciclo(self, v_atual):

        self.ciclo.append(v_atual)
        temp = v_atual
        t_equals_v = False

        while not t_equals_v:

            for a in self.aresta_visitada:
                if a[0] != temp:
                    continue
                elif a[2] is False:
                    a[2] = True
                    v_atual = a[1]
                    self.ciclo.append(v_atual)
                    break
            else:
                print("l 71")
                return False, None

            t_equals_v = temp == v_atual
        # End while

        for a in self.aresta_visitada:
            if a[0] not in self.ciclo:
                continue
            elif a[2] is False:
                r, subciclo = self.alg_subciclo(a[0])
                if r is False:
                    print("l 83")
                    return False, None
                else:
                    index = self.ciclo.index(a[0])
                    list_aux = list()
                    for i in range(index, len(self.ciclo)):
                        list_aux.append(self.ciclo[i])
                    for i in range(index, len(self.ciclo)):
                        self.ciclo.pop()
                    self.ciclo.extend(subciclo)
                    self.ciclo.extend(list_aux)

        print("l 93")
        return True, self.ciclo
