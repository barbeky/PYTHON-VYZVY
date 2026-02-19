# 14. týždeň – Python (Stredná úroveň)
# Úloha: Ulož 5 čísel do zoznamu a pomocou indexov vypíš index + hodnotu a spočítaj súčet.

cisla = []

for i in range(5):
    n = int(input("Zadaj cislo: "))
    cisla.append(n)

print("Zoznam:", cisla)

sucet = 0
for i in range(len(cisla)):
    print("Index", i, "-> hodnota", cisla[i])
    sucet += cisla[i]

print("Sucet:", sucet)
