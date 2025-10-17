def operaciones(num1, num2, operacion="+"):
    """Realiza una operación matemática básica."""
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            raise ValueError("No se puede dividir por cero.")
        return num1 / num2
    else:
        raise ValueError(f"Operación '{operacion}' no soportada.")
    
print("OPERACIONES BASICAS")
while True:
    try:
        n1 = float(input("Ingrese el primer número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

while True:
    try:
        n2 = float(input("Ingrese el primer número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

operacion = input("Ingrese la operación (+, -, *, /): ")

resultado = operaciones(n1, n2, operacion)
print(f"El resultado de {n1} {operacion} {n2} es: {resultado}")