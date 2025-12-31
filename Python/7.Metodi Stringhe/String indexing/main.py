# Indexing = accedere agli elementi di una sequenza tramite []
# Slicing  = [inizio : fine : incremento]
# Nota: l'indice finale è ESCLUSO

carta_di_credito = "1234-5678-9012-3456"

# -------------------------
# ESEMPI DI INDEXING
# -------------------------

# Primo carattere
# print(carta_di_credito[0])

# Ultimo carattere (indice negativo)
# print(carta_di_credito[-1])

# -------------------------
# ESEMPI DI SLICING
# -------------------------

# Primi 4 caratteri (lo 0 può essere omesso)
# print(carta_di_credito[:4])

# Dal 5° carattere fino alla fine
# print(carta_di_credito[5:])

# Tutti i caratteri in posizione pari
# print(carta_di_credito[::2])

# -------------------------
# MASCHERARE NUMERO DI CARTA
# -------------------------

# Prendo gli ultimi 4 caratteri
ultimi_4 = carta_di_credito[-4:]

# Maschero il numero di carta
print(f"XXXX-XXXX-XXXX-{ultimi_4}")

# -------------------------
# INVERTIRE UNA STRINGA
# -------------------------

# Inverte completamente la stringa
carta_invertita = carta_di_credito[::-1]
print(carta_invertita)
