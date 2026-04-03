mena = ["Anna", "Peter", "Eva", "Martin", "Lucia"]

hladane = input("Zadaj meno: ")

nasiel = False

for meno in mena:
    print("Hladam...")
    if meno == hladane:
        print("Nasiel som:", meno)
        nasiel = True
        break

if not nasiel:
    print("Nenasiel som")
