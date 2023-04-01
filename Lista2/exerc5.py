A = int(input("Informe o 1º número: "))
B = int(input("Informe o 2º número: "))
if (B==0):
    print("Impossível dividir por 0")
elif (A%B==0):
    print(A, " é divisível por ", B)
else:
    print(A, " não é divisível por ", B)