n = input("Su quanti numeri vuoi effettuare l'analisi? ")

while not n.isdigit() or int(n) < 1:
    n = input("Numero non valido.\nSu quanti numeri vuoi effettuare l'analisi? ")

n = int(n)

somma = 0
pari = 0
dispari = 0

for i in range(n):
    numero = input(f"Inserire il {i+1}° numero: ")

    while not numero.isdigit():
        numero = input(f"Numero non valido.\nReinserire il {i+1}° numero: ")

    numero = int(numero)
    somma += numero

    if i == 0:
        massimo = numero
        minimo = numero
    else:
        if numero > massimo:
            massimo = numero
        elif numero < minimo:
            minimo = numero

    if numero % 2 == 0:
        pari += 1
    else:
        dispari += 1

media = somma / n

print(
    f"E' stata effettuata l'analisi su {n} numeri.\n"
    f"Max: {massimo}\n"
    f"Min: {minimo}\n"
    f"Somma: {somma}\n"
    f"Media: {media}\n"
    f"Ci sono {pari} numeri pari\n"
    f"E {dispari} numeri dispari"
)
