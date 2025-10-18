# Nombre de Archivo> expresionesRegulares.py
# Expresiones Regulares en Python   
# Las expresiones regulares (regex o regexp) son secuencias de caracteres que forman un patrón de búsqueda. En Python, el módulo 're' proporciona funciones para trabajar con expresiones regulares.
# Sintaxis básica:
# .      : Coincide con cualquier carácter excepto una nueva línea.
# ^      : Coincide con el inicio de una cadena.
# $      : Coincide con el final de una cadena.
# *      : Coincide con cero o más repeticiones del patrón anterior.
# +      : Coincide con una o más repeticiones del patrón anterior.
# ?      : Coincide con cero o una repetición del patrón anterior.
# []     : Coincide con cualquier carácter dentro de los corchetes.
# {}     : Especifica el número de repeticiones del patrón anterior.
# |      : Operador OR, coincide con cualquiera de los patrones separados por el símbolo.

import re
# Ejemplo 1: Buscar una palabra en una cadena
texto = "Hola, bienvenido al mundo de Python. Python es genial."
patron = r"Python"
coincidencias = re.findall(patron, texto)
print("Coincidencias encontradas:", coincidencias)  # Salida: ['Python', 'Python']

# Ejemplo 2: Validar un correo electrónico
correo = "yo@angelamores.com"
patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(patron_correo, correo):
    print("Correo electrónico válido")
else:
    print("Correo electrónico inválido")

# Ejemplo 3: Reemplazar todas las vocales en una cadena por '*'
texto_vocales = "Expresiones regulares en Python"
patron_vocales = r"[aeiouAEIOU]"
texto_modificado = re.sub(patron_vocales, "*", texto_vocales)
print("Texto modificado:", texto_modificado)  # Salida: "Expr*s**n*s r*g*l*r*s *n Pyth*n"

# Ejemplo 4: Dividir una cadena por espacios en blanco
texto_dividir = "Dividir esta cadena en palabras"   
palabras = re.split(r"\s+", texto_dividir)
print("Palabras:", palabras)  # Salida: ['Dividir', 'esta', 'cadena', 'en', 'palabras']

# Ejemplo 5: Encontrar números en una cadena
texto_numeros = "Tengo 2 perros y 3 gatos."
patron_numeros = r"\d+"
numeros_encontrados = re.findall(patron_numeros, texto_numeros)
print("Números encontrados:", numeros_encontrados)  # Salida: ['2', '3']

# Ejemplo 6: Validar un número de teléfono (formato: 123-456-7890)
telefono = "03-2820984"
patron_telefono = r"^\d{2}-\d{7}$"
if re.match(patron_telefono, telefono):
    print("Número de teléfono válido")
else:
    print("Número de teléfono inválido")
