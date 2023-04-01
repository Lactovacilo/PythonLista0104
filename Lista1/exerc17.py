A = str(input("Insira o valor A: "))
B = str(input("Insira o valor B: "))
print("Valores sem mudança: ", A, B)
tempA = A
A = B
B = tempA
print("Valores invertidos: ", A, B)