d = int()
n = int(input("Digite um número Inteiro: "))
for c in range(1, n+1):
    if n % c == 0:
        d += 1

if d < 3:
    print("o número {} é primo".format(n))
else:
    print("o número {} não é primo".format(n))