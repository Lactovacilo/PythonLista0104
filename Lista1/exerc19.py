n = int(input("Insira um número de 3 dígitos: "))
Centena = n//100
Dezena = (n%100)//10
Unidade = n%10

nAmp = n+Unidade*100 + Dezena*10 + Centena
CentenaAmp = nAmp//100
DezenaAmp = (nAmp%100)//10
UnidadeAmp = nAmp%10

Codigo = CentenaAmp*1 + DezenaAmp*2 + UnidadeAmp*3

print("O dígito verificador é: ", (Codigo%10))