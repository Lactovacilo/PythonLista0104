n = int(input("Insira um número de 3 dígitos: "))
Centena = n//100
Dezena = (n%100)//10
Unidade = n%10
print("O número invertido é: ", Unidade, Dezena, Centena)