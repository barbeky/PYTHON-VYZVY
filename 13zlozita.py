import random

cisla = []
for _ in range(10):
    cisla.append(random.randint(1, 50))

print("Zoznam:", cisla)

pocet_parnych = 0
for cislo in cisla:
    if cislo % 2 == 0:
        pocet_parnych += 1

percento = (pocet_parnych / len(cisla)) * 100

print("Počet párnych:", pocet_parnych)
print("Percento párnych:", round(percento, 1), "%")
