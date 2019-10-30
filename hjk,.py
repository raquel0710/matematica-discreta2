N, M = map(lambda i: int(i), input().split( ))
L = []
for i in range(N):
    L.append(input().split())
s = []
K = int(input())
for i in range(K):
    disparo_linha, disparo_coluna = map(lambda i: int(i), input().split( ))
    s.append((disparo_linha, disparo_coluna))

print(L)
print(s)
count = 0
for i in s:
    linha, coluna = i
    if L[i] == "#":
        count += 1
print(count)
