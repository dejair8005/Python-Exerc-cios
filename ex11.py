l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
area = l * a
litro = area * 0.5
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(l, a, area))
print("Para pintar essa parede', você precisará de {}l de tinta".format(litro))