nome = str(input("Qual é o seu nome? ").lower())
if nome == "dejair":
    print("Que nome Bonito")
#elif nome == "ana" or nome == "maria" or nome == "joao":
elif nome in "ana maria joao":
    print("Seu nome é bem popular")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia {}".format(nome))