n = int(input("Número de vértices: ")) #coloca-se o número de vértices
m_adj = [[0 for i in range(n)] for j in range(n)] #a matriz é criada com apenas zeros
for i in range(n):
    m_adj[i] = [int(m) for m in input().split(' ')] #adiciona-se valores binários à matriz
dicio = {} #cria um dicionario para especificar quem é adjacente de quem(passando a matriz para o dicionario)
for i,j in enumerate(m_adj): #processo para selecionar quem são adjacentes de quem e após colocar no dicionário
    r = []
    for l in range(len(j)):
        if j[l] != 0:
            r.append(l)
        dicio[i] = r
print(dicio) 

def pintar_cores(d): #Algoritmo Welsh Powell
    global c
    c = {} #dicionário que associa vértices à suas respectivas cores
    adjacentes = sorted(list(d.keys()), key=lambda x: len(d[x]), reverse=True) #aqueles que possuem mais vizinhos em ordem decrescente
    for i in adjacentes: #cria-se uma lista com a quantidade de vérticessendo que preenchida por True
        cores_possiveis = [True] * len(adjacentes)
        for j in d[i]: #o programa irá percorrer cada vértice e analisar quem são adjacentes de quem, e distribuir as demais cores
            if j in c:
                color = c[j]
                cores_possiveis[color] = False
        for color, possiveis in enumerate(cores_possiveis):
            if possiveis:
                c[i] = color
    return c
print(pintar_cores(dicio)) #printando a distribuição de cores(elas estão em ordem decrescente)

lista_de_cores = [] #lista para armazenar apenas as cores
for i in c.values(): #pegando os valores do dicionario c
    lista_de_cores.append(i) #adicionando apenas as cores à lista
print(len(set(lista_de_cores))) #printando quantas cores foram utilizadas
