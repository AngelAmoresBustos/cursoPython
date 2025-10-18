# Funcion filter() en Python
# La funcion filter() en Python se utiliza para filtrar elementos de una secuencia (como una lista, tupla o conjunto) basándose en una función que devuelve True o False para cada elemento.

# Sintaxis:
# filter(funcion, secuencia)
# Donde:
# funcion: Una función que devuelve True o False para cada elemento de la secuencia.
# secuencia: La secuencia que se va a filtrar (puede ser una lista, tupla, conjunto, etc.).
# Ejemplo 1: Filtrar números pares de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_par(num):
    return num % 2 == 0

# con una funcion normal y común: es_par
numeros_pares = list(filter(lambda num:num % 2 == 0, numeros))
print("Números pares:", numeros_pares)  # Salida: [2, 4, 6, 8, 10]

# con una funcion lambda
numeros_pares = list(filter(lambda num:num % 2 == 0, numeros))
print("Números pares:", numeros_pares)  # Salida: [2, 4, 6, 8, 10]