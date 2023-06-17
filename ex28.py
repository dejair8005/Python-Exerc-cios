import random

print("______________________________________________________")
print("Vou pensar em um numero entre 0 e 5")
print("______________________________________________________")
n = random.randint(0, 5)
p = int(input("Qual número eu pensei? "))
print("Analisando numero pensado")
if n == p:
    print("Parabens! Você acertou")
else:
    print("Não Foi dessa vez")
print("O numero Pensado foi {} e e você disse {}".format(n, p))
