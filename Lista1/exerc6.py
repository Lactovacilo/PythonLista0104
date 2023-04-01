SM = int(input("Insira o salário mínimo: "))
QW = int(input("Insira a quantia de quilowatts gasta: "))
Vqw = SM/700
print("Valor do quilowatt: R$", Vqw)
n = Vqw*QW
print("Valor a ser pago: R$", n)
print("Valor a ser pago com desconto: R$", n*0.9)