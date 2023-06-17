d = int(input("Quantos dias alugados? "))
km = float(input("Quantos  Km rodados? "))
tolal = (60 * d) + (0.15 * km)
print("O total a pagar é de R${:.1f}".format(tolal))