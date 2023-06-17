n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
op = 0

while op != 5:
    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair""")
    op = int(input(">>>>>Qual é sua opção: "))
    if op == 1:
        print("A soma entre {} e {} é {}".format(n1, n2, n1 + n2))
    elif op == 2:
        print("{} x {} = {}".format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print("O maior entre {} e {} é {}".format(n1, n2, n1))
        elif n2 > n1:
            print("O maior entre {} e {} é {}".format(n1, n2, n2))
        else:
            print("Os valores {} e {} são iguais".format(n1, n2))
    elif op == 4:
        print("Informe os numeros novamente")
        n1 = int(input("Primeiro numero: "))
        n2 = int(input("Segundo numero: "))
    else:
        print("Progama finalizado")



    print("==-==-==-==-==-==-==-==-==-==-==")

