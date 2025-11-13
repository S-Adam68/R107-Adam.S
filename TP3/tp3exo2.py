import time

n = int(input("Saisir un nombre entier n positif : "))

for i in range (n,-1,-1):
    time.sleep(1)
    print(i)

while n != -1:
    time.sleep(1)
    print(n)
    n=n-1