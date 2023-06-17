from random import randint
pc = randint(1, 3)

print("Vamos Jogar Jokenpô\n")

print("1 - (Pedra)")
print("2 - (Papel)")
print("3 - (Tesoura)\n")

p = int(input("Digite umas das opções: "))


if p == 1:
    print("Você escolheu Pedra")
    if pc == 1:
        print("O computador escolheu Pedra")
        print("Empate!")

    elif pc == 2:
        print("O computador escolheu Papel")
        print("Você Perdeu!")
    else:
        print("O computador escolheu Tesoura")
        print("Você Ganhou")


elif p == 2:
    print("Você escolheu Papel")
    if pc == 1:
        print("O computador escolheu Pedra")
        print("Você Ganhou")

    elif pc == 2:
        print("O computador escolheu Papel")
        print("Empate!")
    else:
        print("O computador escolheu Tesoura")
        print("Você perdeu")


elif p == 3:
    print("Você escolheu Tesoura")
    if pc == 1:
        print("O computador escolheu Pedra")
        print("Você Perdeu")

    elif pc == 2:
        print("O computador escolheu Papel")
        print("Você ganhou!")
    else:
        print("O computador escolheu Tesoura")
        print("Empate")

else:
    print("Opção inválida!")
