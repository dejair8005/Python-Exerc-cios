media = float()
velho = str()
velhoid = int()
mulheres20 = int()

for x in range(1, 5):
    nome = str(input("Digite o nome de uma pessoa: "))
    id = int(input("Qual a idade dessa pessoa: "))
    sexo = str(input("Sexo dessa pessoa M ou F").upper())

    if x == 1:
        media = id
        velho = nome
        velhoid = id
    else:
        media = (media + id) / x
        if id > velhoid:
            velho = nome
            velhoid = id

    if sexo == "F" and id < 20:
        mulheres20 += 1


print("\nA media das idades é {:.2f}".format(media))
print("Nesse grupo tem {} Mulhere(s) abaixo dos 20".format(mulheres20))
print("A idade do mais velho é {} nome é {}".format(velhoid, velho))


