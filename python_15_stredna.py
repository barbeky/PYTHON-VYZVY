# 15. tyzden - Python - Stredna uroven
# Tema: Prezitie na opustenom ostrove (energia)

energia = 10

while energia > 0:
    print("Tvoja energia:", energia)
    volba = input("Vyber akciu (1 - chodza, 2 - oddych): ")

    if volba == "1":
        energia -= 2
    elif volba == "2":
        energia += 1

print("Dosla ti energia. Hra konci.")
