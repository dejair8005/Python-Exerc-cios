ano = int(input("Qual ano de nascimento do atleta? "))
id = 2023 - ano

print("O atleta tem {} ano(s)".format(id))
if id <= 9:
    print("Categoria:  MIRIM")

elif 9 < id <= 14:
    print("Categoria:  INFANTIL")

elif 14 < id <= 19:
    print("Categoria:  JUNIOR")

elif 19 < id <= 20:
    print("Categoria:  SENIOR")

else:
    print("Categoria:  MASTER")


