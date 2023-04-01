Genero = int(input("Se for homem - Digite 1\nSe for mulher - Digite 0\n"))
Altura = float(input("Digite sua altura (em metros): "))
if (Genero==1):
    print("Peso ideal = ", ((72.7*Altura) - 58), "kg")
else:
    print("Peso ideal = ", ((62.1*Altura) - 44.7), "kg")