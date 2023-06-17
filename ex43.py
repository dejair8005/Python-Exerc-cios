p = float(input("Digite seu peso: "))
a = float(input("Qual sua altura: "))
imc = p / (a * a)

if imc < 18.5:
    print("Imc {:.1f} abaixo do peso".format(imc))

elif 18.5 <= imc < 25:
    print("Imc {:.1f} peso ideal".format(imc))

elif 25 <= imc < 30:
    print("Imc {:.1f} sobre peso".format(imc))

elif 30 <= imc < 40:
    print("Imc {:.1f} obesidade".format(imc))
else:
    print("Imc {:.1f} obesidade morbida".format(imc))


