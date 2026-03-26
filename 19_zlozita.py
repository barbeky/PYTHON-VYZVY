import random

spravne_cislo = random.randint(1, 20)
pokusy = 5
uhadol = False

print("Hadaj cislo od 1 do 20.")

while not uhadol and pokusy > 0:
    tip = int(input("Tvoj tip: "))

    if tip == spravne_cislo:
        uhadol = True
    elif tip < spravne_cislo:
        pokusy = pokusy - 1
        print("Cislo je vacsie. Zostava", pokusy, "pokusy.")
    else:
        pokusy = pokusy - 1
        print("Cislo je mensie. Zostava", pokusy, "pokusy.")

if uhadol:
    print("Uhadol si! Cislo bolo", spravne_cislo)
else:
    print("Prehral si, cislo bolo", spravne_cislo)
