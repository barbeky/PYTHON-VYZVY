# Výzva 27 – ASCII art – Jednoduchá úloha
# Plný obdĺžnik z hviezdičiek

sirka = int(input("Zadaj sirku: "))
vyska = int(input("Zadaj vysku: "))

for riadok in range(vyska):
    for stlpec in range(sirka):
        print("*", end="")
    print()
