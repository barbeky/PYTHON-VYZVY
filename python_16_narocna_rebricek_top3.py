# Náročná úroveň – Rebríček TOP 3

hraci = []

for i in range(3):
    meno = input("Zadaj meno hraca: ")
    body = int(input("Zadaj pocet bodov: "))
    hraci.append([meno, body])

hraci.sort(key=lambda x: x[1], reverse=True)

for i in range(min(3, len(hraci))):
    print(i+1, ".", hraci[i][0], "-", hraci[i][1], "bodov")
