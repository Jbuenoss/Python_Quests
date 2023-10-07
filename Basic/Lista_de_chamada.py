leitor = input()
n = int(leitor.split()[0])
k = int(leitor.split()[1])
chamada = []
for index in range(n):
    s = input()
    chamada.append(s)
chamada.sort()
print(chamada[k-1])