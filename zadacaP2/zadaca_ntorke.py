"""
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.

Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 

Nedovoljan
0-49%

Dovoljan
50-65%

Dobar
65-80%

Vrlodobar
80-90%

Izvrstan
90-100%
"""

rezultati = []

with open('rezultati.csv', 'r') as file:
    for linija in file:
        rezultati.append((ime, prezime, int(bodovi)))

for ime, prezime, bodovi in rezultati:
    if bodovi > 50:
        print(ime, prezime, bodovi)
ocjene = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlo dobar": 0,
    "Izvrstan": 0
}

for ime, prezime, bodovi in rezultati:
    if bodovi < 50:
        ocjene["Nedovoljan"] += 1
    elif bodovi < 65:
        ocjene["Dovoljan"] += 1
    elif bodovi < 80:
        ocjene["Dobar"] += 1
    elif bodovi < 90:
        ocjene["Vrlo dobar"] += 1
    else:
        ocjene["Izvrstan"] += 1


for ocjena in ocjene:
    print(ocjena, ocjene[ocjena])
