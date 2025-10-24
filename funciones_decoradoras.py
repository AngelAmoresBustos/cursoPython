# Nombre de Archivo: funciones_decoradoras.py
# Objetivo: Implementar y demostrar el uso de funciones decoradoras en Python.
# Las funciones decoradoras son una característica poderosa en Python que permite modificar el comportamiento de una función sin cambiar su código.
# Funciones Matemáticas Básicas en Python
# Este archivo contiene funciones para realizar operaciones matemáticas básicas como suma, resta, multiplicación, división y potencia.


def funciones_decoradoras(funcion):
    def envoltura(*args, **kwargs):
        print(f"Ejecutando la función '{funcion.__name__}' con argumentos {args} y {kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"Resultado de la función '{funcion.__name__}': {resultado}")
        return resultado
    return envoltura


@funciones_decoradoras
def sumar(num1, num2):
    return num1 + num2


@funciones_decoradoras
def restar(num1, num2):
    return num1 - num2


@funciones_decoradoras
def multiplicar(num1, num2):
    return num1 * num2


@funciones_decoradoras
def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: División por cero no permitida."


@funciones_decoradoras
def potencia(base, exponente):
    return base ** exponente


# Ejemplos de uso de las funciones
print(sumar(5, 3))          # Salida: 8
print(restar(10, 4))        # Salida: 6 
print(multiplicar(6, 7))    # Salida: 42
print(dividir(20, 5))       # Salida: 4.0
print(potencia(base=2, exponente=3))       # Salida: 8