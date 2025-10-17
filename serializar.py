# manejo de archivo binarios con pickle
# para guardar listas y diccionarios
import pickle

def guardar_datos(lista, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(lista, archivo)

def cargar_datos(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        lista = pickle.load(archivo)
    return lista

# Ejemplo de uso
datos = ['manzana', 'banana', 'cereza'] 
guardar_datos(datos, 'datos.pkl')
datos_cargados = cargar_datos('datos.pkl')  
print(datos_cargados)