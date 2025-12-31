# if = esegue un blocco di istruzioni solo se la condizione è vera
# else = esegue un altro blocco se la condizione è falsa

eta = int(input("Inserisci la tua età: "))

# -------------------------
# IF CON INTERI
# -------------------------

if eta < 0:
    print("Età non valida")
elif eta >= 100:
    print("Sei troppo grande per registrarti")
elif eta >= 18:
    print("Registrato correttamente")
else:
    print("Devi essere maggiorenne per registrarti")

# -------------------------
# IF CON STRINGHE
# -------------------------

scelta = input("Hai fame? (S/N): ").upper()

if scelta == "S":
    print("Buon appetito")
else:
    print("OK")

name = input("Inserisci il tuo nome: ").strip()

if name == "":
    print("Non hai scritto il tuo nome")
else:
    print(f"Ciao {name}")

# -------------------------
# IF CON BOOLEANI
# -------------------------

in_vendita = True

if in_vendita:   # se in_vendita è True
    print("È in vendita")
else:
    print("Non è in vendita")
