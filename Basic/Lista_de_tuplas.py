n = int(input())
lista = []
while n != 0:
    s = input()
    s1 = s.split()[0]
    s2 = s.split()[1]
    lista.append((s1, s2))
    n -= 1
print(lista)
