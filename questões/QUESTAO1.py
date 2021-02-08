def recursividade(n,k):
    if k == 0 or k==n:
        return 1
    else:
        return ((n - k + 1) * recursividade(n, k - 1)) // k



n = int(input("Insira o valor de n: "))
p = int(input("Insira o valor de p: "))
k = p
print(recursividade(n, k))

"comments"

