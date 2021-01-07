lista_nome = []
nome = input("Digite nome (Digite 'Fim' para terminar)")
while nome != "Fim":
    lista_nome.append(nome)
    nome = input("Digite nome (Digite 'Fim' para terminar)")
lista_nomeC = lista_nome[:]
for i in range(len(lista_nome)):
    nome = min(lista_nomeC)
    del lista_nomeC[lista_nomeC.index(nome)]
    print(nome, end = " ")
