operatore = input("Cosa vuoi fare(+ - * /)?  ")
numero1 = int(input("Inserire il primo numero: "))
numero2 = int(input("Inserire il secondo numero: "))

if operatore == "+":
    risultato = numero1+numero2
    print(risultato)
elif operatore == "-":
    risultato = numero1 - numero2
    print(risultato)
elif operatore == "*":
    risultato = numero1 * numero2
    print(risultato)
elif operatore == "/":
    risultato = numero1 / numero2
    print(risultato)
else:
    print(f"Operatore {operatore} non valido")