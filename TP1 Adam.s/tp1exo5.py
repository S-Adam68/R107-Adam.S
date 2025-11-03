Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> jour=3
>>> heure=09
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> heure=9
>>> minute=35
>>> print(minute+heure*60+(jour-1)*1440)
3455
jour=int(input("entrer le jour du mois : "))
heure= int(input("entrer l'heure du jour: "))
minute=int(input("entrer les minutes de l'heure: "))
print(minute+heure*60+(jour-1)*1440,"minutes")
