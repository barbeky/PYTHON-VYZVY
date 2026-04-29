# 24. výzva – Python – Zložitá úloha
# Téma: f-string s viacriadkovým reťazcom a formátovaním (.2f)

meno = input("Meno žiaka: ")

predmety = []
znamky = []

for i in range(3):
    predmet = input(f"Predmet {i + 1}: ")
    znamka = int(input(f"Známka {i + 1}: "))
    predmety.append(predmet)
    znamky.append(znamka)

priemer = sum(znamky) / len(znamky)

vysvedcenie = f"""
===== VYSVEDČENIE =====
Žiak: {meno}
{predmety[0]}: {znamky[0]}
{predmety[1]}: {znamky[1]}
{predmety[2]}: {znamky[2]}
-----------------------
Priemer: {priemer:.2f}
=======================
"""

print(vysvedcenie)
