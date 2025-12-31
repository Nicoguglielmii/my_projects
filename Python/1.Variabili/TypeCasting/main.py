# Il typecasting è quel processo che permette di cambiare il tipo di una variabile in un altro
#                  str(), int(), float(), bool()

nome = "Nicola Guglielmi"
eta = 17
media = 7.1
studente = True

# La funzione type restituisce il tipo della variabile
print(type(nome))

# Int -> Float (aggiunge .0)
eta = float(eta)
print(eta)

# Float -> Int (tronca la parte decimale)
media = int(media)
print(media)

# Int/Float -> String
eta = str(eta)
print(eta, type(eta))  # A noi sembra non sia cambiato niente, ma è cambiato il tipo

# String -> Int / Float
# È possibile solo se la stringa rappresenta un numero valido
nome = "33"
nome = int(nome)
print(nome)

# String -> Boolean
# Se la stringa NON è vuota il valore è True, altrimenti è False
nome = bool(nome)
print(nome)

# Boolean -> Int
# True = 1, False = 0
studente = int(studente)
print(studente)

# Boolean -> Float
studente = float(studente)
print(studente)

# Boolean -> String
studente = str(studente)
print(studente, type(studente))