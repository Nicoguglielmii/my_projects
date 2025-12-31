import math

cateto1 = float(input("Inserire il 1° cateto: "))
cateto2 = float(input("Inserire il 2° cateto: "))

ipotenusa = math.sqrt(pow(cateto1, 2) + pow(cateto2, 2))
print(f"L'ipotenusa è {ipotenusa}")