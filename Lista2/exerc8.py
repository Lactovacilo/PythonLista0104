idade = int(input("Insira sua idade: "))
if (idade >= 1 and idade <= 13):
    print("Você é uma criança")
elif (idade > 13 and idade <= 20):
    print("Você é um adolescente")
elif (idade > 20 and idade <= 50):
    print("Você é um adulto")
elif (idade > 50):
    print("Você é um idoso")
else:
    print("Você inseriu um número inválido")