n = int(input("rentrez un nombre"))
fact = 1
for i in range (1,n+1):
    fact = fact * i
    print(fact)
fact=1
while n != 0 :
    fact = fact * n
    n=n-1
    print (fact )