def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
x = int(input("Digite um numero para calcular o fibonacci: "))
res = fibonacci(x - 1)
print(res)