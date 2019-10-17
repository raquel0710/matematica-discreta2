def dividindo_imperio( i, pai ):
    global resposta
    peso_arestas = 1
    for j in grafo[i]:
        if ( j != pai ):
            peso_arestas += dividindo_imperio( j, i )
    diferenca = abs(N-2*peso_arestas)
    if ( diferenca < resposta ):
        resposta = diferenca
    return peso_arestas

[N] = [int(p) for p in input().split()]
grafo = [[] for _ in range(N+1)]

for i in range(1,N):
    [A, B] = [int(p) for p in input().split()]
    grafo[A].append( B )
    grafo[B].append( A )
resposta = N

dividindo_imperio( 1, -1 )
print(resposta)
