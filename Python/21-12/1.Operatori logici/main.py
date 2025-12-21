# Gli operatori logici servono per combinare più condizioni
# or  → almeno una condizione deve essere vera
# and → tutte le condizioni devono essere vere
# not → nega una condizione

temp = 25
piove = False

# -------------------------
# ESEMPIO CON AND / NOT
# -------------------------

if temp >= 25 and not piove:
    print("Fa caldo e non piove")
elif temp <= 0 and not piove:
    print("Fa freddo e non piove")
elif temp >= 25 and piove:
    print("Fa caldo e piove")
elif temp <= 0 and piove:
    print("Fa freddo e piove")
else:
    print("Temperatura nella norma")

# -------------------------
# ESEMPIO CON OR
# -------------------------

num = int(input("Inserisci un numero maggiore di 10 e minore di 20: "))

if num < 10 or num > 20:
    print("Numero non valido")
else:
    print("Numero valido")
