def je_parne(cislo):
    return cislo % 2 == 0

for i in range(5):
    cislo = int(input("Zadaj cislo: "))
    if je_parne(cislo):
        print(cislo, "je parne")
    else:
        print(cislo, "je neparne")
