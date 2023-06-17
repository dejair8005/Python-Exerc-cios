from math import radians, sin, cos, tan
n = float(input("Valor do angulo: "))
sen = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))

print("O angulo de {} tem seno {:.2f}".format(n, sen))
print("O angulo de {} tem cosseno {:.2f}".format(n, cos))
print("O angulo de {} tem tangente {:.2f}".format(n, tan))