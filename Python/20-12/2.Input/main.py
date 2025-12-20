# input() = Una funzione che permette all'utente di inserire dati
#           Restituisce l'inserimento in una stringa

nome = input("Qual'è il tuo nome? ")
print(f"Ciao {nome}")

# Se dobbiamo prendere in input un intero/float dobbiamo fare il casting
eta = int(input("Quanti anni hai? "))
print(f"Hai {eta} anni!")
