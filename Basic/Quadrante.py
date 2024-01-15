n1 = int(input())
n2 = int(input())
if n1 == 0 or n2 == 0:
    print("eixos")
elif n1 > 0 and n2 > 0:
    print("Q1")
elif n1 > 0:
    print("Q4")
elif n2 > 0:
    print("Q2")
else:
    print("Q3")