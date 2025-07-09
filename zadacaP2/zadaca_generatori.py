
#Napraviti generator funkcije za ispis
#svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.

def parni_neparni():
    for i in range(n):
        if i % 2 == 0:
            yield i "je paran"
        else:
            yield i "je neparan"
for tekst in parni_neparni(n):
    print(tekst)
