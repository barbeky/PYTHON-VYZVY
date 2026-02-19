# 14. týždeň – Python (Zložitá úroveň)
# Úloha: Nájdi najväčšie číslo v zozname a jeho index bez použitia max().

cisla = [3, 8, 11, 20, 7, 4, 9]

max_hodnota = cisla[0]
max_index = 0

for i in range(1, len(cisla)):
    if cisla[i] > max_hodnota:
        max_hodnota = cisla[i]
        max_index = i

print("Zoznam:", cisla)
print("Najvacsie cislo:", max_hodnota)
print("Je na indexe:", max_index)
