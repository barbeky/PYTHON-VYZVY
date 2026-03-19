znamky = {"Anna": 1, "Peter": 3, "Eva": 2, "Martin": 4}

for meno, znamka in znamky.items():
    print(meno + ": " + str(znamka))

najlepsi = None
najlepsia_znamka = 5

for meno, znamka in znamky.items():
    if znamka < najlepsia_znamka:
        najlepsia_znamka = znamka
        najlepsi = meno

print("Najlepsi student: " + najlepsi + " (znamka " + str(najlepsia_znamka) + ")")
