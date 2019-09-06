v = int(input("Digite aqui o número de vértices: "))
a = int(input("Digite aqui o número de arestas: "))
matriz = [[0 for i in range(v)] for j in range(v)]

for i in range(a):
    v1, v2 = input("Insira as arestas: ").split(" ")
    v1 = int(v1)
    v2 = int(v2)
    matriz[v1][v2] = 1

for i in range(v):
    print(matriz[i])

lista_graus = []
for i in range(v):
    print()
    adj = 0
    for j in range(v):
        if matriz[i][j] == 1: adj = adj + 1
    lista_graus.append(adj)
    print("Província {} possui {} vizinhos".format(i+1, adj))
lista_graus.sort(reverse=True)
print(lista_graus)
