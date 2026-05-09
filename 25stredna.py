def vacsi(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Zadaj prvé číslo: "))
b = int(input("Zadaj druhé číslo: "))
print("Väčšie číslo je:", vacsi(a, b))
