ano = int(input("Digite um ano? "))
r = ano % 4

if r == 0:
    print("{} é um ano Bissexto".format(ano))
else:
    print("{} não é um ano Bissexto".format(ano))