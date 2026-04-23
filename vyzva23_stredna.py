veta = input("Zadaj vetu: ")

pocet_medzier = veta.count(" ")
pocet_pismen = len(veta) - pocet_medzier
pocet_slov = len(veta.split())

print("Pocet pismen:", pocet_pismen)
print("Pocet medzier:", pocet_medzier)
print("Pocet slov:", pocet_slov)
