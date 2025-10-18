# Funcion map() en Python
# La funcion map() en Python se utiliza para aplicar una funcion a cada elemento de una secuencia (como una lista, tupla o conjunto) y devolver un nuevo iterable con los resultados.
# Sintaxis:
# map(funcion, secuencia)
# Donde:
# funcion: Una función que se aplicará a cada elemento de la secuencia.
# secuencia: La secuencia cuyos elementos se van a procesar (puede ser una lista, tupla, conjunto, etc.).
# Ejemplo 1: Elevar al cuadrado cada número en una lista    

numeros = [1, 2, 3, 4, 5]

def elevar_al_cuadrado(num):
    return num ** 2

# con una funcion normal y común: elevar_al_cuadrado
cuadrados = list(map(elevar_al_cuadrado, numeros))
print("Números al cuadrado:", cuadrados)  # Salida: [1, 4, 9, 16, 25]

# con una funcion lambda
cuadrados = list(map(lambda num: num ** 2, numeros))
print("Números al cuadrado:", cuadrados)  # Salida: [1, 4, 9, 16, 25]

# Ejemplo 2: Convertir una lista de temperaturas en Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

# con una funcion normal y común: celsius_a_fahrenheit
fahrenheit = list(map(celsius_a_fahrenheit, celsius))
print("Temperaturas en Fahrenheit:", fahrenheit)  # Salida: [32.0, 50.0, 68.0, 86.0, 104.0]

# con una funcion lambda    
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Temperaturas en Fahrenheit:", fahrenheit)  # Salida: [32.0, 50.0, 68.0, 86.0, 104.0]

# Ejemplo 3: Convertir una lista de cadenas a mayúsculas 
cadenas = ["hola", "mundo", "python", "es", "genial"]

def upper_case(s):
    return s.upper()

# con una funcion normal y común: upper_case
mayusculas = list(map(upper_case, cadenas))
print("Cadenas en mayúsculas:", mayusculas)  # Salida: ['HOLA', 'MUNDO', 'PYTHON', 'ES', 'GENIAL']

# con una funcion lambda   
mayusculas = list(map(lambda s: s.upper(), cadenas))
print("Cadenas en mayúsculas:", mayusculas)  # Salida: ['HOLA', 'MUNDO', 'PYTHON', 'ES', 'GENIAL']

print(cadenas)

print(mayusculas)