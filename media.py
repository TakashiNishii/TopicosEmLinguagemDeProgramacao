idade = 1
soma = 0
quant = 0
while idade != 0:
    idade = int(input())
    if (idade > 0):
        soma = soma + idade
        quant = quant + 1
print("%.2f"%(soma/quant))
