n = int()

for c in range(1, 6):
     if c == 1:
         n2 = int(input("Digite um número: "))
         if n2 % 2 == 0:
             n += n2

     n2 = int(input("Digite outro número: "))
     if n2 % 2 == 0:
         n += n2

print("A soma é {}".format(n))