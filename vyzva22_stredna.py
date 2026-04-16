import random

def pozdrav():
    meno = input("Zadaj meno: ")
    print("Ahoj, " + meno + "!")

def kalkulacka():
    cislo1 = int(input("Zadaj prvé číslo: "))
    cislo2 = int(input("Zadaj druhé číslo: "))
    print("Súčet:", cislo1 + cislo2)

def nahodny_citat():
    citaty = [
        "Kto neriskuje, nepije šampanské.",
        "Bez práce nie sú koláče.",
        "Učenie je svetlo, neučenie je tma.",
        "Kto sa smeje naposledy, ten sa smeje najlepšie."
    ]
    citat = random.choice(citaty)
    print("Citát dňa:", citat)

while True:
    print("=== MENU ===")
    print("1 - Pozdrav")
    print("2 - Kalkulačka")
    print("3 - Náhodný citát")
    print("4 - Koniec")

    volba = input("Tvoja voľba: ")

    if volba == "1":
        pozdrav()
    elif volba == "2":
        kalkulacka()
    elif volba == "3":
        nahodny_citat()
    elif volba == "4":
        print("Dovidenia!")
        break
    else:
        print("Neplatná voľba.")
