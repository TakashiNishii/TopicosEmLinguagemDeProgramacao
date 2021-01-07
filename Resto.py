num = 0
soma = 0
while (num <= 0):
    num = int(input())
while (num > 10):
    soma = soma + int(num%10)
    num = num/10
soma = soma + int(num)
print("%d"%soma)
