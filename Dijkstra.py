N, A, B = map(lambda i: int(i), input().split())
A-=1
B-=1
#Matriz de adjacencias
G = [[0 for i in range(N)] for j in range(N)]
for i in range(N-1):
        P, Q, D = map(lambda i: int(i), input().split())
        P-=1
        Q-=1
        G[P][Q]=D
        G[Q][P] = D
        print(G)

#DIC = {0:0} #0,D = origem, custo
DIC = {str(i):float("inf") for i in range(N)}
DIC[str(A)]=0
print(DIC)

L= [(0,A)]


def Distancia():
    while L!=[]:
        custo, va = L.pop(0)
        for i in range(N):
            if G[va][i]:
                if DIC[str(i)] > G[va][i] + custo:
                    DIC[str(i)]=G[va][i]+ custo
                    L.append((DIC[str(i)],i))

    
Distancia()
print(DIC[str(B)])
