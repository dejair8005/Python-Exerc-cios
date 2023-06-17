a = int(input("Digite o primero lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))
if (a + b > c) and (c + b > b) and ( a + c > b):
    if a == b == c:
        print("Todos os lados são iguais: EQUILATERO")
    elif a != b != c:
        print("Todos os lados são diferentes: ESCALENO")
    else:
        print("Dois lados são iguais:  ISOCELES")
else:
    print("Não é um Triângulo")