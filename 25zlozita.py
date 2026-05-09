def obvod(a, b):
    return 2 * (a + b)

def obsah(a, b):
    return a * b

def je_stvorec(a, b):
    return a == b

a = int(input("Zadaj stranu a: "))
b = int(input("Zadaj stranu b: "))

print("Obvod:", obvod(a, b))
print("Obsah:", obsah(a, b))
print("Je to štvorec:", je_stvorec(a, b))
