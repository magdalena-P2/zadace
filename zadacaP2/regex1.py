"""Napisati regex za provjeru validnosti unosa e-maila.
E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji
mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost),
a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
"""
import re
unos1=input("Unesi mail adresu: ")

reg = "[a-zA-Z]+[a-zA-Z]+@fpmoz.sum.ba$"
result = re.findall(reg, unos1)
print(result)

unos1 = input("Unesi eduId:")
reg1 ="^[a-zA-Z][a-zA-Z]+[0-9]*@sum.ba$"
result1 = re.findall(reg1, unos1)

print(result1)

if result and result1:
    print("Mail i eduId su ispravni!")
