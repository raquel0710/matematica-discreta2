lista = [] #lista em que vou adicionar tuplas compostas por (altura do retângulo, índice(posição do retângulo))
N = int(input()) #número de retângulos
alturas = [int(i) for i in input().split()] #armazenando as alturas em uma lista
for i in range(len(alturas)): 
    lista.append((alturas[i],i+1)) #adicionando tuplas à lista compostas por altura, índice(posição do retângulo)
lista.sort() #ordenando a lista em ordem crescente

marcador = [1 for i in range(N+2)] #marcador associando os retângulos percorridos como 0
marcador[0]= 0                      #e os não percorridos à 1
marcador[N+1]=0                     #marcador tipo [0,N,0]

respostatemporaria = 2 #número máximo de pedaços cortados
respostafinal = 2

for i in lista: #percorrendo a lista
    alturas, indice = i #para percorrer a altura e o índice(posição do retângulo) dentro das tuplas
    respostafinal = max(respostafinal, respostatemporaria) #a resposta final sempre vai ser o maior entre a resposta final e a resposta temporaria analisada
    marcador[indice] = 0 #associando o marcador a lista de tuplas e marcando com 0 o que está sendo verificado
    if marcador[indice-1] == 1 and marcador[indice+1] == 1: #retângulo menor que o anterior e o posterior, somar + 1 pedaço
        respostatemporaria += 1
    if marcador[indice-1] == 0 and marcador[indice+1] == 0: #retângulo maior que o anterior e o posterior, - 1 pedaço
        respostatemporaria -= 1
print(respostafinal) #printar o valor máximo encontrado, ou seja, a resposta final

