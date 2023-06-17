from random import randint

p = int
numero = int(randint(1, 10))


print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 e 10")
print("Será que voce consegue adivinha qual foi?")

palpites = 0
while p != numero:
    numero = int(randint(1, 10))
    p = int(input("Qual seu palpite "))

    if p == numero:
        print("O número sorteado foi {} e vc disse {}".format(numero, p))
    else:
        print("O número sorteado foi {} tente novamete!".format(numero))
        palpites += 1
print("O numero de palpites foi {}".format(palpites))