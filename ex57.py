
sx = str(input("Informe se sexo: [M/F] ")).strip().upper()[0]


while sx not in "mMfF":
    sx = input("Dados invalidos. Por favor, informe seu sexo: ")

print("Sexo {} Registrado Com Sucesso".format(sx))

