lista = [] #lista em que vou adicionar tuplas compostas por (altura do retângulo, índice)
N = int(input()) #número de retângulos
alturas = [int(i) for i in input().split()] #armazenando as alturas em uma lista
for i in range(len(alturas)): 
    lista.append((alturas[i],i+1)) #adicionando tuplas à lista compostas por altura, índice
lista.sort() #ordenando a lista em ordem crescente

marcador = [1 for i in range(N+2)] #marcador associando os retângulos percorridos como 0
marcador[0]= 0                      #e os não percorridos à 1
marcador[N+1]=0                     #marcados tipo [0,N,0]

respostatemporaria = 2 #número mínimo de corte
respostafinal = 2

for i in lista:
    alturas, indice = i
    respostafinal = max(respostafinal, respostatemporaria)
    marcador[indice] = 0
    if marcador[indice-1] == 1 and marcador[indice+1] == 1:
        respostatemporaria += 1
    if marcador[indice-1] == 0 and marcador[indice+1] == 0:
        respostatemporaria -= 1
print(respostafinal)
