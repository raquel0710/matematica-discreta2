N,M = [int(x) for x in input().split()]
tab = []
for x in range(N):
    linha = list(input())[:M]
    tab.append(linha)

lisnums = [1]

def check(c):
    Y = tab.index(p)
    X = p.index(c)
    try:
        if tab[Y][X] == "#" and type(tab[Y-1][X]) == int:
            if Y > 0:
                tab[Y][X] = tab[Y-1][X]
    except IndexError:
        None
    try:
        if tab[Y][X] == "#" and type(tab[Y][X-1]) == int:
            if X > 0:
                tab[Y][X] = tab[Y][X-1]
    except IndexError:
        None
    try:
        if tab[Y][X] == "#" and type(tab[Y][X+1]) == int:
            if X < (len(tab[Y])-1):
                tab[Y][X] = tab[Y][X+1]
    except IndexError:
        None
    try:
        if tab[Y][X] == "#" and type(tab[Y+1][X]) == int:
            if Y < (len(tab)-1):
                tab[Y][X] = tab[Y+1][X]
    except IndexError:
        None 
    if tab[Y][X] == "#":
        if len(lisnums) == 0:
            lisnums.append(1)
        tab[Y][X] = lisnums[-1]
        lisnums.append(lisnums[-1]+1)
    ########
    try:
        if type(tab[Y][X]) == int and tab[Y-1][X] == "#":
            if Y > 0:
                tab[Y-1][X] = tab[Y][X]
    except IndexError:
        None
    try:
        if type(tab[Y][X]) == int and tab[Y][X-1] == "#":
            if X > 0:
                tab[Y][X-1] = tab[Y][X]
    except IndexError:
        None
    try:
        if type(tab[Y][X]) == int and tab[Y][X+1] == "#":
            if X < 0:
                tab[Y][X+1] = tab[Y][X]
    except IndexError:
        None
    try:
        if type(tab[Y][X]) == int and tab[Y+1][X] == "#":
            if Y < (len(tab)-1):
                tab[Y+1][X] = tab[Y][X]
    except IndexError:
        None
    ########   

for p in tab:
    for c in p:
        if c == "#":
            check(c)

K = int(input())
for t in range(K):
    L,C = [int(x) for x in input().split()]
    if type(tab[L-1][C-1]) == int:
        tab[L-1][C-1] = "X"

res = 0
lisfin = []
for h in tab:
    for r in h:
        if type(r) == int:
            lisfin.append(r)

for s in lisnums:
    if s not in lisfin:
        res+=1

if res == 0:
    print(res)
elif res > 0:
    print(res-1)
