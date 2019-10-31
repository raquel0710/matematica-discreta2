N, P = map(lambda i: int(i), input().split())
valores = []
pesos = []
for i in range(N):
    peso, valor = map(lambda i: int(i), input().split())
    valores.append(valor)
    pesos.append(peso)
valores.sort()
pesos.sort()

def juvenal(N, P, valores, pesos):
    K = [[0 for x in range(P+1)] for x in range(N+1)] 
    for i in range(N+1): 
        for peso in range(P+1): 
            if i==0 or peso==0: 
                K[i][peso] = 0
            elif pesos[i-1] <= peso: 
                K[i][peso] = max(valores[i-1] + K[i-1][peso-pesos[i-1]],  K[i-1][peso]) 
            else: 
                K[i][peso] = K[i-1][peso] 
  
    return K[N][P] 

print(juvenal(N, P, valores, pesos)) 
