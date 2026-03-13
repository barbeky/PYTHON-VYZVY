# 17. tyzden: Narocna uloha - Text medzi znakmi
text = str(input("Zadaj text: "))

# Najdeme poziciu otvaracej a zatvaracej zatvorky
start_index = text.find('<')
end_index = text.find('>')

# Slicing: text medzi zatvorkami
vysledok = text[start_index + 1 : end_index]

print("Medzi zatvorkami je: ", vysledok)
