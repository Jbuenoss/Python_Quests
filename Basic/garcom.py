resp = 0
n = int(input())
for index in range(n):
    leitor = input()
    n1 = int(leitor.split()[0])
    n2 = int(leitor.split()[1])
    if(n1 > n2):
        resp += n2
print(resp)