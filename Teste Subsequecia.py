n = int(input())
sequencia = 1
auxSeq = 1
num = float(input())
ant = num
for i in range(n - 1):
    ant = num
    num = float(input())
    if (num > ant):
        auxSeq = auxSeq + 1
    else:
        if(auxSeq > sequencia):
            sequencia = auxSeq
        auxSeq = 1
if(auxSeq > sequencia):
    sequencia = auxSeq
    auxSeq = 1
print(sequencia)
