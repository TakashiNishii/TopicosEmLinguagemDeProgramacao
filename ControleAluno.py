def criaMatriz(totAlu):
    matriz = []
    for i in range(totAlu):
        linha = []
        for c in range(1):
            linha.append(input("Digite o nome do "+str(i+1)+"o aluno: "))
            linha.append(float(input("Digite a primeira nota dele(a): ")))
            linha.append(float(input("Digite a segunda nota dele(a): ")))
            linha.append(float(input("Digite a terceira nota dele(a): ")))
        matriz.append(linha)
    return matriz
            
def escreveMatriz(mat, linha):
    for i in range(totAlu):
        for c in range(1):
            if (c == 0):
                print("Aluno =", end=" ")
                print(mat[i][0])
            else:
                print("",end="\t")
                print("Nota 1: %.1f"%mat[i][1],end=" - ")
                print("Nota 2: %.1f"%mat[i][2],end=" - ")
                print("Nota 3: %.1f"%mat[i][3],end=" => ")
                print("Média: ")
                media = (mat[i][1] + mat[i][2] + mat[i][3])/3
                print("%.1f"%media)
        print()
totAlu = int(input("Defina a quantidade de alunos: "))
while(totAlu <= 0 or totAlu > 20):
    totAlu = int(input("Defina a quantidade de alunos: "))
listaAlu = criaMatriz(totAlu)
escreveMatriz(listaAlu, totAlu)
