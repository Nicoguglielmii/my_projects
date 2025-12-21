# -------------------------
# METODI DELLE STRINGHE
# -------------------------

nome = input("Inserisci il tuo nome: ")

# La funzione len() restituisce il numero di caratteri presenti nella stringa
# lunghezza = len(nome)

# Il metodo find() restituisce la posizione del carattere passato come parametro
# Viene restituita la PRIMA occorrenza
# Il primo carattere ha indice 0
# Se il carattere non è presente restituisce -1
# risultato = nome.find(" ")

# Il metodo rfind() (reverse find) restituisce la posizione
# dell'ULTIMA occorrenza del carattere
# risultato = nome.rfind("a")

# Il metodo capitalize() rende maiuscolo solo il primo carattere
# nome = nome.capitalize()

# Il metodo upper() rende tutti i caratteri maiuscoli
# nome = nome.upper()

# Il metodo lower() rende tutti i caratteri minuscoli
# nome = nome.lower()

# Il metodo isdigit() restituisce True se la stringa contiene SOLO numeri
# nome = nome.isdigit()

# Il metodo isalpha() restituisce True se la stringa contiene SOLO lettere
# NOTA: se contiene spazi o caratteri speciali restituisce False
# nome = nome.isalpha()

# -------------------------
# ESEMPIO CON NUMERO DI TELEFONO
# -------------------------

numero_di_telefono = input("Inserisci il tuo numero di telefono: ")

# Il metodo count() restituisce quante volte
# un carattere (o stringa) è presente
# risultato = numero_di_telefono.count("-")

# Il metodo replace() permette di sostituire un carattere con un altro
# numero_di_telefono = numero_di_telefono.replace("-", "/")

# La funzione help() mostra la documentazione completa
# dei metodi disponibili per il tipo di dato
# print(help(str))
