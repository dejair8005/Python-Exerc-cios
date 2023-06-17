ano = int(input("Em qual ano você nasceu? "))
id = int(2023 - ano)
if id < 18:
    print("Você ainda vai se alistar \n")
    falta = 18 - id
    print("Você tem {} anos e faltam {} ano(s) para o alistamento".format(id, falta))
elif id == 18:
    print("Você tem {} anos e já é a hora de se alistar".format(id))
else:
    print("Você tem {} anos e já passou da hora de se alistar".format(id))
