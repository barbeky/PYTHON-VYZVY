import random

cisla = []
for i in range(5):
    cislo = random.randint(1, 100)
    cisla.append(cislo)

print("Vygenerované čísla:", cisla)
print("Najväčšie:", max(cisla))
print("Najmenšie:", min(cisla))
