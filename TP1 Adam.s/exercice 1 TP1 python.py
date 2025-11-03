Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=254
>>> type(a)
<class 'int'>
>>> data1=10
>>> data2=11
>>> print(data1, data2)
10 11
>>> 
>>> 
>>> 
>>> nom=Adam
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    nom=Adam
NameError: name 'Adam' is not defined
>>> nom='Adam'
>>> nom='Sebar'
>>> prenom='Adam'
>>> math='14'
>>> info='16'
>>> math= 14
>>> info=16
>>> anglais=13
>>> promotion=1
>>> anglais= 13.5
>>> m=(math+anglais+info)/3
>>> print (m)
14.5
>>> type(m,info,math,anglais)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    type(m,info,math,anglais)
TypeError: type() takes 1 or 3 arguments
>>> type(m)
<class 'float'>
>>> type(info)
<class 'int'>
>>> type(anglais)
<class 'float'>
>>> type(math)
<class 'int'>
>>> L’étudiant toto titi de la promotion 2025 a une moyenne de 12,5
SyntaxError: invalid character '’' (U+2019)
>>> 
>>> 
>>> print("l'étudiant {} {} de la promotion {} a une moyenne de {}".format(prenom, nom, promotion, m))
l'étudiant Adam Sebar de la promotion 1 a une moyenne de 14.5
>>> promotion = 2025
>>> print("l'étudiant {} {} de la promotion {} a une moyenne de {}".format(prenom, nom, promotion, m))
l'étudiant Adam Sebar de la promotion 2025 a une moyenne de 14.5
