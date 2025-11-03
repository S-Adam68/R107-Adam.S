print("Donner les trois nombres entiers x1, x2 et x3 : ")
x1 = int(input("valeur de x1"))
x2 = int(input("valeur de x2"))
x3 = int(input("valeur de x3"))


if(x1==x2 or x3==x1 or x2==x3) :
    print(str(x1==x2 or x3==x1 or x2==x3)+" = VRAI")
else :
    print(str(x1==x2 or x3==x1 or x2==x3)+" = FAUX")
