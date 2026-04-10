import random


def pozdrav():
    meno = input("Zadaj meno: ")
    print("Ahoj, " + meno + "!")


def hadaj_cislo():
    cislo = random.randint(1, 5)
    tip = int(input("Tipni číslo od 1 do 5: "))
    if tip == cislo:
        print("Správne!")
    else:
        print("Nesprávne, správne číslo bolo " + str(cislo) + ".")


while True:
    print("=== MENU ===")
    print("1 - Pozdrav")
    print("2 - Hádaj číslo")
    print("3 - Koniec")

    volba = input("Tvoja voľba: ")

    if volba == "1":
        pozdrav()
    elif volba == "2":
        hadaj_cislo()
    elif volba == "3":
        print("Dovidenia!")
        break
    else:
        print("Neplatná voľba.")
