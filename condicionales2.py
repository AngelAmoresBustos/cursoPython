print("Asignaturas optativas 2025")
print("1. Programación")
print("2. Diseño de páginas web")
print("3. Sistemas de gestión de bases de datos")
asignatura = input("Escriba el número de la asignatura escogida: ")
if asignatura in ("1", "2", "3"):
    print("Asignatura escogida: ", asignatura)
else:
    print("La asignatura escogida no es correcta")  