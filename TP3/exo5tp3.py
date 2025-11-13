

debut = int(input("Entrez l'heure de début de la location : "))
fin = int(input("Entrez l'heure de fin de la location : "))

while debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
    debut = int(input("Entrez l'heure de début de la location : "))
    fin = int(input("Entrez l'heure de fin de la location : "))

while debut == fin:
    print("Attention ! l'heure de fin est identique à l'heure de début.")
    debut = int(input("Entrez l'heure de début de la location : "))
    fin = int(input("Entrez l'heure de fin de la location : "))

while debut > fin:
    print("Attention ! le début de la location est après la fin ...")
    debut = int(input("Entrez l'heure de début de la location : "))
    fin = int(input("Entrez l'heure de fin de la location : "))

tarif = 0
for heure in range(debut, fin):
    if (0 <= heure < 7) or (17 <= heure < 24):
        tarif += 1
    elif 7 <= heure < 17:
        tarif += 2

print(f"Le coût de la location est de {tarif} euros.")
