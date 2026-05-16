import random

tajne = random.randint(1, 50)
limit = random.randint(5, 10)
print(f"Máš {limit} pokusov.")

pokusy = 0
male = 0
velke = 0
tip = 0
uhádol = False

while tip != tajne and pokusy < limit:
    tip = int(input("Hádaj číslo od 1 do 50: "))
    pokusy += 1

    if tip < tajne:
        print("Príliš malé!")
        male += 1
    elif tip > tajne:
        print("Príliš veľké!")
        velke += 1
    else:
        print("Správne!")
        uhádol = True

if not uhádol:
    print(f"Prehral si! Číslo bolo {tajne}.")

print("---")
print(f"Počet pokusov: {pokusy}")
print(f"Príliš malých: {male}")
print(f"Príliš veľkých: {velke}")
if uhádol:
    print("Uhádol si v limite!")
else:
    print("Nevošiel si do limitu.")
