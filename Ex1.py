mat = []
somas = []
def preencheMatriz(mat, lin, col):
    for l in range(lin):
        linha = []
        for c in range(col):
            print("",c+1,"º número da",str(l+1) + "a linha da matriz: ",end="")
            valor = int(input())
            linha.append(valor)
        mat.append(linha)
    return mat

def mostraMatriz(mat, lin, col):
    print("Matriz: ")
    for l in range(lin):
        for c in range(col):
            print(mat[l][c], end = "\t")
        print()
        
def somaColunas(mat, vet, lin, col):
    for c in range(col):
        somas.append(0)
    for l in range(lin):
        for c in range(col):
            somas[c] = somas[c] + mat[l][c]
    return somas
def mostraVetor(vet,col):
    print("Soma das colunas: ")
    for c in range(col):
        print(vet[c], end = "\t")


lin = int(input("Quantas linhas terá sua matriz? "))
col = int(input("Quantas colunas terá sua matriz? "))

mat = preencheMatriz(mat,lin,col)
mostraMatriz(mat,lin,col)
somas = somaColunas(mat,somas,lin,col)
mostraVetor(somas,col)
