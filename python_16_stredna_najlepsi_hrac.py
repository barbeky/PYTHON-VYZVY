# Stredná úroveň – Najlepší hráč

hraci = []

for i in range(3):
    meno = input("Zadaj meno hraca: ")
    body = int(input("Zadaj pocet bodov: "))
    hraci.append([meno, body])

vitaz = hraci[0]

for hrac in hraci:
    if hrac[1] > vitaz[1]:
        vitaz = hrac

print("Vitaz je", vitaz[0], "s", vitaz[1], "bodmi.")
