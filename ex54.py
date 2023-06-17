maior = int()
menor = int()
for c in range(1, 8):
    if c == 1:
        ano = int(input("Digite o ano de nascimento de uma pessoa: "))
    else:
        ano = int(input("Digite o ano de nascimento de outra pessoa: "))

    idade = 2023 - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print("\n Maiores: {}".format(maior))
print("Menores: {}".format(menor))