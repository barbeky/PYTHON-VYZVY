# Jednoduchá úroveň – Zoznam hráčov

hraci = []

for i in range(3):
    meno = input("Zadaj meno hraca: ")
    body = int(input("Zadaj pocet bodov: "))
    hraci.append([meno, body])

print(hraci)
