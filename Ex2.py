def soma(n1,n2):
    print(n1,"+",n2,"=",n1 + n2)
def subtrai(n1,n2):
    print(n1,"-",n2,"=",n1 - n2)
def multiplica(n1,n2):
    print(n1,"*",n2,"=",n1 * n2)
def divide(n1,n2):
    print(n1,"/",n2,"=",n1 / n2)
def lerNums():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1,n2 
def menu():
    n1,n2 = lerNums()
    print()
    op = " "
    while(op != "F"):
        print("[+] Somar")
        print("[-] Subtração")
        print("[*] Multiplicar")
        print("[/] Dividir")
        print("[L] Ler outros números")
        print("[F] Finalizar o programa")
        op = input("Digite sua opção: ")
        print()
        if(op == "+"):
            soma(n1,n2)
        elif(op == "-"):
            subtrai(n1,n2)
        elif(op == "*"):
            multiplica(n1,n2)
        elif(op == "/"):
            divide(n1,n2) 
        elif(op == "L"):
           n1,n2 = lerNums()
        print()
menu()
