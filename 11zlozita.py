slovo = input("Zadaj slovo: ")
pocet = int(input("Zadaj pocet opakovani: "))


def vypis_slovo(slovo, pocet):
    for i in range(pocet):
        print(slovo)


vypis_slovo(slovo, pocet)