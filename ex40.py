n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = float((n1 + n2) / 2)

if m < 5.0:
    print("Sua média é {} você está REPROVADO".format(m))
elif 5.0 <= m <= 6.9:
    print("Sua média é {} você está de RECUPERAÇAO".format(m))
else:
    print("Sua média é {} você está APROVADO".format(m))