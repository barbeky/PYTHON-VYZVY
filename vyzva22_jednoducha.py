def pozdrav():
    meno = input("Zadaj meno: ")
    print("Ahoj, " + meno + "!")

def kalkulacka():
    cislo1 = int(input("Zadaj prvé číslo: "))
    cislo2 = int(input("Zadaj druhé číslo: "))
    print("Súčet:", cislo1 + cislo2)

while True:
    print("=== MENU ===")
    print("1 - Pozdrav")
    print("2 - Kalkulačka")
    print("3 - Koniec")

    volba = input("Tvoja voľba: ")

    if volba == "1":
        pozdrav()
    elif volba == "2":
        kalkulacka()
    elif volba == "3":
        print("Dovidenia!")
        break
    else:
        print("Neplatná voľba.")
