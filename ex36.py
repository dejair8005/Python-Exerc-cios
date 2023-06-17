valor = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o seu salário: R$"))
vezes = int(input("Quantas prestações: "))

prestacao = valor / vezes

if prestacao < (salario / 100 * 30):
    print("Empréstimo Aprovado")
    print("Será pago em {}x de {}R$".format(vezes, prestacao))
else:
    print("Valor da Prestação supera os 30% do salário")