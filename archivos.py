from io import open

def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido


def escribir_archivo(ruta, contenido):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)


def anexar_archivo(ruta, contenido):
    with open(ruta, 'a', encoding='utf-8') as archivo:
        archivo.write(contenido)


def leer_lineas(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    return lineas


def contar_palabras(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
    return len(palabras)


def copiar_archivo(ruta_origen, ruta_destino):
    with open(ruta_origen, 'r', encoding='utf-8') as archivo_origen:
        contenido = archivo_origen.read()
    with open(ruta_destino, 'w', encoding='utf-8') as archivo_destino:
        archivo_destino.write(contenido)

# Ejemplo de uso
escribir_archivo('ejemplo.txt', 'Hola, mundo!\n')
print(leer_archivo('ejemplo.txt'))
anexar_archivo('ejemplo.txt', 'Esta es una línea añadida.\n')
print(leer_archivo('ejemplo.txt'))
print("Lectura de archivo en lista: ", leer_lineas('ejemplo.txt'))
print("Contar palabras del archivo: ", contar_palabras('ejemplo.txt'))
copiar_archivo('ejemplo.txt', 'copia_ejemplo.txt')