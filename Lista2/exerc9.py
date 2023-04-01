salarioBruto = float(input("Insira o salário bruto: "))
proventos = float(input("Insira os proventos"))
if (salarioBruto <= 5000):
    print("O salário líquido é: R$", (salarioBruto + proventos - (salarioBruto/20)))
else:
    print("O salário líquido é: R$", (salarioBruto + proventos - (salarioBruto/10)))