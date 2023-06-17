v = int(input("Digite a velocidade de um carro? "))
print("Sua velocidade é {}km/h".format(v))
if v > 80:
    print("Cuidado você está acima da velocidade!")
    m = (v - 80) * 7
    print("Você vai pagar uma multa de {}R$".format(m))
else:
    print("Parabens! Você está em velocidade permitida")


