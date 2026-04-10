while True:
    print("=== MENU ===")
    print("1 - Povedz ahoj")
    print("2 - Koniec")

    volba = input("Tvoja voľba: ")

    if volba == "1":
        print("Ahoj! Vitaj v programe!")
    elif volba == "2":
        print("Dovidenia!")
        break
    else:
        print("Neplatná voľba.")
