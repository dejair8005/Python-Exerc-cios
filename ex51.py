a1 = int(input("Digite o primeiro Termo: "))
r = int(input("Digite a razão da PA: "))

print("\na1: {}".format(a1))
for c in range(1, 10):
    an = a1 + c * r
    print("a{}: {}".format(c + 1, an))
