import math

strana = float(input("Zadaj stranu štvorca: "))

obvod = 4 * strana
obsah = strana ** 2
uhlopriecka = math.sqrt(2) * strana

print(f"Obvod: {obvod:.2f}")
print(f"Obsah: {obsah:.2f}")
print(f"Uhlopriečka: {uhlopriecka:.2f}")
