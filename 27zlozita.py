# Výzva 27 – ASCII art – Zložitá úloha
# Vycentrovaná pyramída z hviezdičiek

vyska = int(input("Zadaj vysku: "))

for i in range(1, vyska + 1):
    print(" " * (vyska - i) + "*" * (2 * i - 1))
