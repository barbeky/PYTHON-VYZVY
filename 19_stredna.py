spravne_heslo = "python123"

heslo = input("Zadaj heslo: ")

while heslo != spravne_heslo:
    print("Nespravne heslo, skus znova.")
    heslo = input("Zadaj heslo: ")

print("Pristup povoleny!")
