# 15. tyzden - Python - Jednoducha uroven
# Tema: Prezitie na opustenom ostrove (energia)

energia = 10

for i in range(3):
    print("Tvoja energia:", energia)
    volba = input("Vyber akciu (1 - chodza, 2 - oddych): ")

    if volba == "1":
        energia -= 2
    elif volba == "2":
        energia += 1

print("Koniec hry. Finalna energia:", energia)
