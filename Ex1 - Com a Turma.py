def preencheMatriz(mat, lin, col):
    for l in range(lin):
        linhas = []
        for c in range(col):
            linhas.append(int(input(str(c+1)+"º número da "+str(l+1)+"a linha da matriz: ")))
        mat.append(linhas)   
        
def mostraMatriz(mat, lin, col):
    print("Matriz: ")
    for l in range(lin):
        for c in range(col):
            print(mat[l][c], end = "\t")
        print()
        
def somaColunas(mat,vet,lin,col):
    for c in range(col):
        somas = 0
        for l in range(lin):
            somas += mat[l][c]
        vet.append(somas)
        
def mostraVetor(vet, col):
    print("\nSoma das colunas: ")
    for c in range(col):
        print(vet[c],end = "\t")

mat = []
vet = []
lin = int(input("Quantas linhas terá sua matriz? "))
col = int(input("Quantas colunas terá sua matriz? "))
preencheMatriz(mat,lin,col)
mostraMatriz(mat,lin,col)
somaColunas(mat,vet,lin,col)
mostraVetor(vet,col)
