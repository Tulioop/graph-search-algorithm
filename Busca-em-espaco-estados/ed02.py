from pyamaze import maze, agent
from random import randint
from bfs import *
from dfs import *
from aStar import *

def execucaoMaze(tamanho=30, possibilidadeCaminhos=10, algoritmo="aStar"):
    
    goalX, goalY = randint(1,tamanho), 1
    
    m = maze(tamanho,tamanho)
    m.CreateMaze(goalX, goalY, loopPercent=possibilidadeCaminhos)
    
    # Inclusao do agente no ambiente
    a = agent(m,footprints=True, shape="arrow")
    b = agent(m,footprints=True, color='red', filled=True)

    #m.run()

    if algoritmo == "bfs":
        print("Executando a busca em largura")
        path1 = bfs(m)
        path2 = bfs(m)
    else:
        if algoritmo == "dfs":
            print("Executando a busca em profundidade")
            path1 = dfs(m)
            path2 = dfs(m)
        else:
            if algoritmo == 'aStar':
                print("Executando a busca A*")
                path1 = a_star(m)
                path2= a_star(m)
            else:
                path = m.path

  
    m.tracePath({a:path1, b:path2})
    m.run()





if __name__=='__main__':
    execucaoMaze(tamanho=10, algoritmo="aStar")