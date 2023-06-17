maior = float()
menor = float()
for c in range(1, 6):
    if c == 1:
        peso = float(input("Digite o peso de uma pessoa: "))
        maior = peso
        menor = peso
    else:
        peso = float(input("Digite o peso de outra pessoa: "))

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print("\nO maior peso é {:.2f}KG".format(maior))
print("O menor peso é {:.2f}KG".format(menor))