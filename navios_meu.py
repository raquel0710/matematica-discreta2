N, M = map(lambda i: int(i), input().split( ))
LISTA = []
for i in range(N):
    LISTA.append(input().split())

lista_numeros = [1]

def checando_navios(caractere):
    Y = LISTA.index(linha_matriz)
    X = linha_matriz(item)

    if LISTA[Y][X] == "#" and type(LISTA[Y-1][X]) == int:
        if Y > 0:
            LISTA[Y][X] = LISTA[Y-1][X]
    
    if LISTA[Y][X] == "#" and type(LISTA[Y][X-1]) == int:
        if X > 0:
            LISTA[Y][X] = LISTA[Y][X-1]

    if LISTA[Y][X] == "#" and type(LISTA[Y][X+1]) == int:
            if X < (len(LISTA[Y])-1):
                LISTA[Y][X] = LISTA[Y][X+1]
    
    if LISTA[Y][X] == "X" and type(LISTA[Y+1][X]) == int:
        if Y < (len(LISTA) - 1):
            LISTA[Y][X] = LISTA[Y+1][X]
    
    if LISTA[Y][X] == "#":
        if len(lista_numeros) == 0:
            lista_numeros.append(1)
        LISTA[Y][X] = lista_numeros[-1]
        lista_numeros.append(lista_numeros[-1]+1)

    if type(LISTA[Y][X]) == int and LISTA[Y-1][X] == "#":
        if Y > 0:
            LISTA[Y-1][X] = LISTA[Y][X]


    if type(LISTA[Y][X]) == int and LISTA[Y][X-1] == "#":
        if X > 0:
            LISTA[Y][X-1] = LISTA[Y][X]
 
    if type(LISTA[Y][X]) == int and LISTA[Y][X+1] == "#":
        if X < 0:
            LISTA[Y][X+1] = LISTA[Y][X]
 
    if type(LISTA[Y][X]) == int and LISTA[Y+1][X] == "#":
        if Y < (len(L)-1):
            LISTA[Y+1][X] = LISTA[Y][X]

for linha_matriz in LISTA:
    for item in linha_matriz:
        if item == "#":
            checando_navios()

K = int(input())
for t in range(K):
    L,C = [int(x) for x in input().split()]
    if type(LISTA[L-1][C-1]) == int:
        LISTA[L-1][C-1] = "X"

count = 0
listafinal = []
for qualquer in LISTA:
    for qualquer1 in qualquer:
        if type(qualquer1) == int:
            listafinal.append(qualquer1)

for s in lista_numeros:
    if s not in lista_numeros:
        count += 1

if count == 0:
    print(count)
elif count > 0:
    print(count-1)
