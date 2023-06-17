n = int(input("Digite um número? "))
r = n % 2
if r != 0:
    print("Você digitou o número {}, e é IMPAR".format(n))
else:
    print("Você digitou o número {}, e é PAR".format(n))