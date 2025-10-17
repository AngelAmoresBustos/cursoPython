correcto = False
email = input("Ingresa tu email: ")
for i in range(len(email)):
    if email[i] == "@":
        correcto = True
        break   

if correcto:
    print("Email correcto") 
else:
    print("Email incorrecto")
