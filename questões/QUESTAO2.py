print('lista de vértices: A,B,C,D,E,F,G')
inicio = 0
chegada = 0

def inicio_algoritmo():
    global inicio
    global chegada
    inicio = input("Vértice ponto de partida: ")

    chegada = input("Vértice ponto de chegada: ")


grafo = { "A" : { "B" : 5, "D":1, "E":4 },
          "B" : { "A":3, "C":5,"G":7 },
          "C" : { "D":13,"B":5, "C": 1},
          "D" : { "B": 3, "D":10, "G":1 },
          "E" : { "F":8,"C":10,"G":9 },
          "F" : { "G":5, 'E':3,'F':3},
          'G' : { "D":8, "E":9, "G":6, "F":7}}


def destino(grafo, origem, fim):

    controle = {}
    distanciaPresente = {}
    noPresente = {}
    naoPassou = []
    atual = origem
    noPresente[atual] = 0

    for vertice in grafo.keys():
        naoPassou.append(vertice)
        distanciaPresente[vertice] = float('inf')

    distanciaPresente[atual] = [0, origem]

    naoPassou.remove(atual)

    while naoPassou:
        for vizinho, peso in grafo[atual].items():
            pesoCalc = peso + noPresente[atual]
            if distanciaPresente[vizinho] == float("inf") or distanciaPresente[vizinho][0] > pesoCalc:
                distanciaPresente[vizinho] = [pesoCalc, atual]
                controle[vizinho] = pesoCalc
                print(controle)

        if controle == {}: break
        minVizinho = min(controle.items(), key=lambda x: x[1])
        atual = minVizinho[0]
        noPresente[atual] = minVizinho[1]
        naoPassou.remove(atual)
        del controle[atual]

    print("A menor distância entre %s e %s é: %s" % (origem, fim, distanciaPresente[fim][0]))
    print("O menor caminho é: %s" % printPath(distanciaPresente, origem, fim))


def printPath(distancias, inicio, fim):
    if fim != inicio:
        return "%s -- > %s" % (printPath(distancias, inicio, distancias[fim][1]), fim)
    else:
        return inicio

inicio_algoritmo()
destino(grafo, inicio, chegada)
