slovo = input("Zadaj slovo: ")

otocene = slovo[::-1]
print("Otocene slovo:", otocene)

if slovo == otocene:
    print("Slovo je palindrom!")
else:
    print("Slovo nie je palindrom.")
