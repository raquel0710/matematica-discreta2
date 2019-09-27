N, origem, destino = map(lambda i: int(i), input().split()) #adicionando o número de cdds, a cidade de origem e a cidade destino
L = [[] for i in range(N)] #criando listas de acordo com a quantidade de cidades(vértices)
for i in range(N - 1):
    P, Q, D = map(lambda i: int(i), input().split()) #adicionando demais cidades e seu custo
    L[P - 1].append((Q - 1, D)) 
    L[Q - 1].append((P - 1, D))

origem -= 1
destino -= 1

mark = [False] * N #lista para verificar os vértices à medida que forem sendo visitados
Queue = [(0, origem)]  #custo e origem
mark[origem] = True #vértice de origem já verificado


while Queue != []:
    x, y = Queue.pop(0) #retirando o vértice
    if y == destino: #caso o vértice seja igual ao destino
        print(x) #printa o custo e o programa para
        break
    else:
        for i in L[y]:
            if mark[i[0]] == False: #caso o vértice não tenha sido ainda visitado
                Queue.append((i[1] + x, i[0])) #adiciona ele a fila para ser atualizado
                mark[i[0]] = True
