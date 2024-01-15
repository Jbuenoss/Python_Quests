n = int(input())

leitor = input()
listaStr = leitor.split(' ')
listaInt = [int(x) for x in listaStr] 
n1 = listaInt[0]
seq = 1
resp = 1
for index in range(1, n, 1):
    n2 = listaInt[index]
    if(n2 == n1):
        n1 = n2
        seq += 1
        resp = max(resp, seq)
    else:
        n1 = n2
        resp = max(resp, seq)
        seq = 1
print(resp)