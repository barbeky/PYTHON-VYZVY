veta = input("Zadaj vetu: ")

slova = veta.split()

pocty = {}

for slovo in slova:
    if slovo in pocty:
        pocty[slovo] = pocty[slovo] + 1
    else:
        pocty[slovo] = 1

print(pocty)
