aux = 0
pt = 0
ut = 0

while (pt < 1 or ut < 1):
    if (pt < 1):
        pt = int(input())
    if (ut < 1):
        ut = int(input())
if (pt > ut):
    aux = pt
    pt = ut
    ut = aux
for i in range(pt, ut + 1):
    for j in range(1,11):
        print(i*j,end="\t")
    print("")
