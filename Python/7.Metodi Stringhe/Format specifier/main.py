# format specifiers = specificatori di formato
# {:flags} formattano un valore in base ai flag inseriti

prezzo1 = 3.14159
prezzo2 = -987.65
prezzo3 = 12.34

# .(number)f → arrotonda a un certo numero di decimali
print(f"{prezzo1:.2f}")
print(f"{prezzo3:.1f}")

# :(number) → alloca un certo numero di spazi
print(f"{prezzo1:10}")
print(f"{prezzo3:10}")

# :03 → padding con zeri
print(f"{prezzo3:06.2f}")

# :< → allineamento a sinistra
print(f"{prezzo1:<10}")

# :> → allineamento a destra
print(f"{prezzo1:>10}")

# :^ → centrato
print(f"{prezzo1:^10}")

# :+ → mostra sempre il segno
print(f"{prezzo1:+}")
print(f"{prezzo2:+}")

# := → segno nella posizione più a sinistra
print(f"{prezzo2:=10}")

# : (spazio) → spazio prima dei numeri positivi
print(f"{prezzo1: }")
print(f"{prezzo2: }")

# :, → separatore delle migliaia
print(f"{prezzo2:,.2f}")


