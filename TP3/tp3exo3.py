import random

print("Le jeux commence !")
x = random.randint(0,100)
a=int(input("Rentrez un nombre entre 0 et 100 : "))
c=1


while a != x:
    if a<x:
        print("Mauvaise réponse, nombre mystère est plus grand. ")
    else:
        print("Mauvaise réponse, nombre mystère est plus petit. ")
    print("Tentative : ", c)
    a=int(input("Rentrez une nouvelle fois nombre entre 0 et 100 : "))
    c += 1
print ("t cho")


