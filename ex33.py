n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

if n1 < n2 and n1 < n3:
    menor = n1
if n1 > n2 and n1 > n3:
    maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n2 > n1 and n2 > n3:
    maior = n2

if n3 < n1 and n3 < n2:
    menor = n3
if n3 > n2 and n3 > n2:
    maior = n3

print("O menor valor é {}".format(menor))
print("O maior valor é {}".format(maior))