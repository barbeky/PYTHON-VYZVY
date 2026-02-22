# 15. tyzden - Python - Zlozita uroven
# Tema: Prezitie na opustenom ostrove (energia)
# Bonus: hladanie jedla s nahodou

import random

energia = 10

while energia > 0:
    print("Tvoja energia:", energia)
    volba = input("Vyber akciu (1 - chodza, 2 - oddych, 3 - hladanie jedla): ")

    if volba == "1":
        energia -= 2
    elif volba == "2":
        energia += 1
    elif volba == "3":
        if random.randint(0, 1) == 1:
            print("Nasiel si jedlo! +3 energia")
            energia += 3
        else:
            print("Nenasiel si nic.")

print("Dosla ti energia. Hra konci.")
