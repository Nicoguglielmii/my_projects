unita_di_misura = input("Qual'è l'unità di misura(K, L) ? ")
peso_iniziale = float(input("Quanto pesa? "))

if(unita_di_misura == "K"):
    peso_finale = peso_iniziale * 2.205
    print(f"{round(peso_iniziale, 1)} kg sono {round(peso_finale, 1)} lb")
elif(unita_di_misura == "L"):
    peso_finale = peso_iniziale / 2.205
    print(f"{peso_iniziale} lb sono {peso_finale} kg")
else:
    print(f"{unita_di_misura} non è un'unità di misura non valida")