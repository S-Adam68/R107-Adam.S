n=int(input("entrer un nombre entier :"))

if n < 0:
    signe="négatif"

elif n > 0:
    signe="positif"

else:
    signe="zéro"


if n % 2 ==0:
    parite ="pair"
else:
    parite ="impair"

if n == 0:
    print("Le nombre est zéro (et il est pair)")
else:
    print(f"Le nombre est {signe} et {parite} :")


