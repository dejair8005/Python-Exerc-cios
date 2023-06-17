n = int(input("Digite um numero inteiro: "))
print('''Digite uma das opções de conversão abaixo: ")
1 (Binário)
2 Octal
3 (Hexadecimal)''')
op = int(input("Qual opção:  "))

if op == 1:
    print("{} convertido para binário {}".format(n, bin(n)[2:]))

elif op == 2:
    print("{} convertido para octal {}".format(n, oct(n)[2:]))
elif op == 3:
    print("{} convertido para hexadecimal {}".format(n, hex(n)[2:]))

else:
    print("você digitou {} OPÇAO INVALIDA".format(op))