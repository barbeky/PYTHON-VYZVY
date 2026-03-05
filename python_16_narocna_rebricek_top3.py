# Náročná úroveň – Rebríček TOP 3 
# Tabuľka hráčov je zoznam zoznamov: [meno, body]

hraci = []

for i in range(3):
    meno = input("Zadaj meno hraca: ")
    body = int(input("Zadaj pocet bodov: "))
    hraci.append([meno, body])

# 1. miesto
prvy = hraci[0]
for hrac in hraci:
    if hrac[1] > prvy[1]:
        prvy = hrac

# 2. miesto
druhy = None
for hrac in hraci:
    if hrac != prvy:
        if druhy is None or hrac[1] > druhy[1]:
            druhy = hrac

# 3. miesto
treti = None
for hrac in hraci:
    if hrac != prvy and hrac != druhy:
        if treti is None or hrac[1] > treti[1]:
            treti = hrac

print("Rebricek TOP 3:")
print("1.", prvy[0], "-", prvy[1], "bodov")
print("2.", druhy[0], "-", druhy[1], "bodov")
print("3.", treti[0], "-", treti[1], "bodov")
