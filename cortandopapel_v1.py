lista = []
N = int(input()) #número de retângulos
alturas = [int(i) for i in input().split()] #armazenando as alturas em uma lista
for i in range(len(alturas)): 
    lista.append((alturas[i],i+1)) #adicionando tuplas à lista compostas por altura, índice
lista.sort() #ordenando a lista em ordem crescente

marcador = [1 for i in range(N+2)] #marcador associando os retângulos percorridos como 0
marcador[0]= 0                      #e os não percorridos à 1
marcador[N+1]=0                     #marcados tipo [0,N,0]

RGlobal = 2
RLocal = 2 #número mínimo de corte
for i in lista: #percorrendo a lista
     alturas, index=i #alturas, índices iguais à i, ou seja vou percorrer as tuplas
     RGlobal = max(RGlobal, RLocal) #o valor global sempre vai ser o maior entre o global e o local
     marcador[index] = 0 #associando o marcador aos índices das tuplas
     if marcador[index-1]==1 and marcador[index+1]==1: #condições para o corte
        RLocal+=1
     if marcador[index-1]==0 and marcador[index+1]==0: #condições para o corte
        RLocal-=1
print(RGlobal) #printar o valor máximo encontrado, ou seja, o global
