Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> minute_total=int(input("Donnez le nombre de minute écoulé depuis le début du mois : "))
Donnez le nombre de minute écoulé depuis le début du mois : 1533
>>> jour=minute_total%1440+1
>>> jour=minute_total//1440+1
>>> tmp=minute_total%1440
>>> heure= tmp//60
>>> minute=tmp%60
>>> print("Nous sommes le jour : ",jour,", à : ",heure, "h et ", minute,"minutes")
Nous sommes le jour :  2 , à :  1 h et  33 minutes
