
#a)
N= int(input("rentre le nombre "))
somme = 0
for i in range (1, N+1) :
    somme = somme + i
print(somme)

#b)
n= int(input("rentrer un nombre "))
while n != 100:
    n = int(input("rentrer un nombre "))

#c)

plus10 = 0
egale10etmoin15 = 0
plus15 = 0

for i in range (+9):
    n = float(input("rentrez un nombre en 0 et 20 : "))
    while n<0 or n>20:
        n = float(input("rentrez un nombre en 0 et 20 : "))
    if n<10:
        plus10=plus10 + 1
    elif 10 <= n <15:
        egale10etmoin15=egale10etmoin15 + 1
    else:
        plus15 = plus10 + 1
print ("nombre de valeurs inférieur strictement à 10 ", plus10)
print ("nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15",egale10etmoin15)
print ("nombre de valeurs supérieur ou égale à 15 ", plus15)

#d)
x=int(input("donné une valeur pour x : "))
somme = 0
N = 0
while somme + N <= x :
    somme += N
    N += 1
print("Le plus grand nombre est : " , N - 1)
print ("La somme correspondante est : ", somme)





