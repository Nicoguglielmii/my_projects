import random

tentativi = 0
indovinato = False
numero_generato = random.randint(1, 100)

while not indovinato:
    numero_utente = int(input("Inserire un numero compreso tra 1 e 100: "))
    
    while numero_utente < 1 or numero_utente > 100:
        numero_utente = int(input(f"Il Numero {numero_utente} non valido.\nReinserire il numero: "))
    
    tentativi += 1
    if (numero_utente > numero_generato):
        print("Numero troppo alto!")
    elif (numero_utente < numero_generato):
        print("Numero troppo piccolo!")
    else: 
        print(f"Numero indovinato dopo {tentativi} tentativi!\nEra {numero_generato}")
        indovinato = True

print("Programma terminato.")