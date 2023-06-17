s = int()
for n in range(1, 501):
    if n % 2 != 0:
        if n % 3 == 0:
            s += n
print("A soma é {}".format(s))