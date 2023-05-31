<<<<<<< HEAD
import heapq
=======
from collections import deque
>>>>>>> a99984671e8df833a37e4738b8d73b59196b1fa8
import random
from befirst import calcular_vizinho

def busca_custo_minimo(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
<<<<<<< HEAD
    fronteira = []
    nosVisitados = set()
    heapq.heappush(fronteira, (0, inicio))
    custoMinimoPath = {}

    while fronteira:
        custo, vertice = heapq.heappop(fronteira)
=======
    fila = deque()
    nosVisitados = set()
    fila.append(inicio)
    aStarPath = {}

    while fila:
        vertice = fila.popleft()
>>>>>>> a99984671e8df833a37e4738b8d73b59196b1fa8
        nosVisitados.add(vertice)

        if vertice == labirinto._goal:
            print("Objetivo encontrado")
            break

        movimentos = ["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d]:
<<<<<<< HEAD
                vizinho = calcular_vizinho(vertice, d)
                if vizinho not in nosVisitados:
                    novo_custo = custo + 1
                    heapq.heappush(fronteira, (novo_custo, vizinho))
                    custoMinimoPath[vizinho] = vertice
=======
                if d == 'E':
                    vizinho = (vertice[0], vertice[1] + 1)
                if d == 'W':
                    vizinho = (vertice[0], vertice[1] - 1)
                if d == 'N':
                    vizinho = (vertice[0] - 1, vertice[1])
                if d == 'S':
                    vizinho = (vertice[0] + 1, vertice[1])

                if vizinho not in nosVisitados:
                    fila.append(vizinho)
                    aStarPath[vizinho] = vertice
>>>>>>> a99984671e8df833a37e4738b8d73b59196b1fa8

    caminho_percorrido = []
    cell = labirinto._goal
    caminho_percorrido.append(cell)
    while cell != inicio:
<<<<<<< HEAD
        fwdPath[custoMinimoPath[cell]] = cell
        cell = custoMinimoPath[cell]

    return fwdPath
=======
        cell = aStarPath[cell]
        caminho_percorrido.append(cell)

    distancia_total = len(caminho_percorrido) - 1

    print("Distância total percorrida:", distancia_total)
    print("Caminho percorrido:")
    for cell in reversed(caminho_percorrido):
        print(cell)



# import random

# # Custo acumulado (distância percorrida desde o início)


# def custo(labirinto):
#     inicio = (labirinto.rows, labirinto.cols)
#     fronteira=[]
#     nosVisitados=[]
#     fronteira.append(inicio)
#     custoPath={}

#     def cost(cell):
#      return custoPath[cell]

#     while fronteira != []:
#         # Ordenar a fronteira pelo custo acumulado para garantir que o caminho mais promissor seja explorado primeiro
#         fronteira.sort(key=lambda x: x[1])
#         vertice, custo_atual = fronteira.pop(0)
#         nosVisitados.append(vertice)

#         if vertice == labirinto._goal:
#             print("Objetivo encontrado")
#             break

#         movimentos = ["E", "S", "N", "W"]
#         random.shuffle(movimentos)

#         for d in movimentos:
#             if labirinto.maze_map[vertice][d] == True:
#                 if d == 'E':
#                     vizinho = (vertice[0], vertice[1] + 1)
#                 if d == 'W':
#                     vizinho = (vertice[0], vertice[1] - 1)
#                 if d == 'N':
#                     vizinho = (vertice[0] - 1, vertice[1])
#                 if d == 'S':
#                     vizinho = (vertice[0] + 1, vertice[1])

#                 if vizinho not in nosVisitados:
#                     if vizinho not in [x[0] for x in fronteira]:
#                         fronteira.append((vizinho, custo_atual + 1))
#                         custoPath[vizinho] = custo_atual + 1

#     #Construção do caminho
#     caminhoTotal = []
#     cell = labirinto._goal
#     caminhoTotal.append(cell)
#     while cell != inicio:
#         cell = custoPath[cell]
#         caminhoTotal.append(cell)
    
#     print("Distancia percorrida:", len(caminhoTotal) - 1)

#     fwdPath = {}
#     cell = labirinto._goal
#     while cell != inicio:
#         fwdPath[custoPath[cell]] = cell
#         cell = custoPath[cell]
#     return fwdPath
>>>>>>> a99984671e8df833a37e4738b8d73b59196b1fa8
