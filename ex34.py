s = float(input("Qual o valor do sálário? "))
if s > 1250:
    aumento = s * 1.1
    taxa = 10
else:
    aumento = s * 1.15
    taxa = 15
print("O salário inicial é {:.2f} com o aumento de {}% de aumente você passa a receber {:.2f} R$".format(s, taxa, aumento))