d = int(input("Qual a distância da viagem? "))
if d <= 200:
    preco = float(d * 0.5)
else:
    preco = float(d * 0.45)

print("A viagem é de {}km e você vai pagar {}R$".format(d, preco))