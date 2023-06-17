a = int(input("Digite o primero lado do triângulo? "))
b = int(input("Digite o segundo lado do triângulo? "))
c = int(input("Digite o terceiro lado do triângulo? "))
if (a + b > c) and (c + b > b) and ( a + c > b):
    print("E um triângulo")
else:
    print("Não é um triângulo")
