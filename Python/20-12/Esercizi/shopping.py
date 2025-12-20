elemento = input("Cosa vorresti comprare? ")
prezzo_elemento = float(input("Qual'è il prezzo? "))
quantita_elemento = int(input("Quante ne vorresti prendere? "))

prezzo_finale = prezzo_elemento * quantita_elemento
print(f"Hai comprato {quantita_elemento} {elemento} a {prezzo_finale} euro")