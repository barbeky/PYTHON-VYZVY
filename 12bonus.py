def kalkulacka(a, b, operacia):
    if operacia == "+":
        return a + b
    elif operacia == "-":
        return a - b
    elif operacia == "*":
        return a * b
    elif operacia == "/":
        if b == 0:
            print("Neda sa delit nulou.")
            return 0
        return a / b  
    else:
        print("Neznama operacia.")
        return 0

a = int(input("Zadaj a: "))
b = int(input("Zadaj b: "))
operacia = input("Zadaj operaciu (+, -, *, /): ")

vysledok = kalkulacka(a, b, operacia)
print("Vysledok:", vysledok)
