p = float(input("Qual o preço do produto? R$ "))
print("Escolha umas condições abaixo: \n")
print("1 - A vista dinheiro/cheque")
print("2 - A vista no cartão")
print("3 - Em 2x no cartão")
print("4 - Em 3x ou mais")
op = int(input("Digite uma das opções acima:  "))

if op == 1:
    pd = p * 0.90
    print("\nVocê escolheu a opção a vista dinheiro/cheque")
    print("Preço normal R${}, preço com desconto de 10% R${}".format(p, pd))

if op == 2:
    pd = p * 0.95
    print("\nVocê escolheu a opção a vista no cartão")
    print("Preço normal R${}, preço com desconto de 5% R${}".format(p, pd))

if op == 3:
    pd = p / 2
    print("\nVocê escolheu a opção a pagar em 2X")
    print("Você vai pagar em 2x de R${}".format(pd))

if op == 4:
    v = int(input("\nEm quantas vezes você quer pagar: "))
    pd = (p * 1.20) / v
    print("Você vai pagar em {}x de R${}".format(v, pd))



