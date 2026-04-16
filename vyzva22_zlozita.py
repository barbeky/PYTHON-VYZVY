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

def kviz():
    otazky = [
        "Hlavné mesto Slovenska? ",
        "Koľko je 7 * 8? ",
        "Aká farba má tráva? "
    ]
    odpovede = [
        "Bratislava",
        "56",
        "zelená"
    ]

    spravne = 0

    for i in range(len(otazky)):
        odpoved = input("Otázka " + str(i + 1) + ": " + otazky[i])
        if odpoved == odpovede[i]:
            spravne = spravne + 1

    print("Tvoje skóre:", spravne, "z", len(otazky))

while True:
    print("=== MENU ===")
    print("1 - Pozdrav")
    print("2 - Kalkulačka")
    print("3 - Náhodný citát")
    print("4 - Kvíz")
    print("5 - Koniec")

    volba = input("Tvoja voľba: ")

    if volba == "1":
        pozdrav()
    elif volba == "2":
        kalkulacka()
    elif volba == "3":
        nahodny_citat()
    elif volba == "4":
        kviz()
    elif volba == "5":
        print("Dovidenia!")
        break
    else:
        print("Neplatná voľba.")
