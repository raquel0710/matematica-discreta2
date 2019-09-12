n = int(input("Número de vértices: "))
m_adj = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    m_adj[i] = [int(m) for m in input().split(' ')]
dicio = {}
for i,j in enumerate(m_adj):
    r = []
    for l in range(len(j)):
        if j[l] != 0:
            r.append(l)
        dicio[i] = r
print(dicio)

def pintar_cores(d):
    global c
    c = {}
    adjacentes = sorted(list(d.keys()), key=lambda x: len(d[x]), reverse=True)
    for i in adjacentes:
        cores_possiveis = [True] * len(adjacentes)
        for j in d[i]:
            if j in c:
                color = c[j]
                cores_possiveis[color] = False
        for color, possiveis in enumerate(cores_possiveis):
            if possiveis:
                c[i] = color
    return c
print(pintar_cores(dicio))

lista_de_cores = []
for i in c.values():
    lista_de_cores.append(i)
print(len(set(lista_de_cores)))
