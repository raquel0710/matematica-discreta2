#Alturas = [(h, indice)]
alturas = []
L = []
N = int(input())
for i in range(N):
    h = int(input())
    alturas.append((h,i+1))
    L.append(h)
print(alturas)
print(L)

alturas.sort(key = lambda x: x[0])

#MARCADOR
#flag = [0,N,0]
#for n in range(1, N+1):
#verificados = [False] * N


#CORTAR PEDAÇOS
pedaços = 1
for i in range(L):
    if 
