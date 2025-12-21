unita_di_misura = input("Qual'è l'unità di misura(C, F) ? ")
temperatura_iniziale = float(input("Qual'è la temperatura? "))

if(unita_di_misura == "C"):
    temperatura_finale = temperatura_iniziale * (9/5) + 32
    print(f"{round(temperatura_iniziale,1)} C° sono {round(temperatura_finale,1)} F°")
elif(unita_di_misura == "F"):
    temperatura_finale = (temperatura_iniziale - 32) * (5/9)
    print(f"{round(temperatura_iniziale,1)} F° sono {round(temperatura_finale,1)} C°")
else:
    print(f"{unita_di_misura} non è un'unità di misura non valida")