def generador_pares(n):
    """Generador de pares de números."""
    for i in range(n):
        yield i * 2


def generador_impares(n):
    """Generador de impares de números."""
    for i in range(n):
        yield i * 2 + 1

def genberador_letras(*palabras):
    """Generador de letras de palabras."""
    for palabra in palabras:
            yield from palabra

pares = generador_pares(5)
impares = generador_impares(5)
letras = genberador_letras("hola", "mundo")

print(list(pares))    
print(list(impares))  

print(next(letras))
print(next(letras))
print(list(letras))