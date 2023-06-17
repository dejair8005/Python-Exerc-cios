import math
co = float(input("Digite  o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
h = math.hypot(co, ca)
print("O valor da hipotenusa desse triangulo retângulo é {:.2f}".format(h))