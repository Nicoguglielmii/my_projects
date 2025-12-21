# controlla inserimento username
# 1. username non può essere più lungo di 12 caratteri
# 2. username non può contenere spazi
# 3. username non può contenere numeri

username = input("Inserire l'username: ")

# if len(username) <= 12 and username.find(" ") == -1 and not username.isdigit():
    
if len(username) > 12:
    print(f"L'username non può avere più di 12 caratteri, ne hai inseriti {len(username)}")
elif username.find(" ") > 0:
    print("L'username non può contenere spazi")
elif username.isdigit():
    print("L'username non può contenere numeri")
else:
    print(f"Benvenuto {username}")