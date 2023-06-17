num = int(input("Informe um número: "))
#n = str(num)
un = num // 1 % 10
dz = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print("Analisando o Número {} \n".format(num))
print("Unidade: {}".format(un))
print("Dezena: {}".format(dz))
print("Centena: {}".format(cen))
print("Milhar: {}".format(mil))