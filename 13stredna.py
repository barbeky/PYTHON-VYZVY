cisla = []

for _ in range(5):
    cislo = int(input("Zadaj celé číslo: "))
    cisla.append(cislo)

print("Zoznam:", cisla)

priemer = sum(cisla) / len(cisla)
print("Priemer:", priemer)
