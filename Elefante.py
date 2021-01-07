n = int()

def musicaElefantes(n):
    for i in range(n):
        print(i+1, end=" ")
        if (i == 0):
            print("elefante incomoda", end=" ")
        else:
            print("elefantes", end=" ")
        if((i+1)%2 == 0):
            print("incomodam muito mais")
        elif(i > 0):
            for j in range(i-1):
                print("incomodam,", end=" ")
            print("incomodam muita gente")
            
            
while(n < 1 or n > 20):
    n = int()

musicaElefantes(n)
