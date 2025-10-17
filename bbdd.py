import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pruebas"
)

# Crear un cursor
cursor = conexion.cursor()

# Función para crear un nuevo tipo de documento
def crear_tipo_documento(codigo, nombre, estado):
    sql = "INSERT INTO tipodocumento (codigo, nombre, estado) VALUES (%s, %s, %s)"
    valores = (codigo, nombre, estado)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tipo de documento creado con éxito.")


# Función para leer todos los tipos de documentos
def leer_tipos_documentos():
    sql = "SELECT * FROM tipodocumento"
    cursor.execute(sql)
    tipos_documentos = cursor.fetchall()
    for tipo_documento in tipos_documentos:
        print(tipo_documento)


# Función para actualizar un tipo de documento por su id
def actualizar_tipo_documento(id, codigo, nombre, estado):
    sql = "UPDATE tipodocumento SET codigo = %s, nombre = %s, estado = %s WHERE id = %s"
    valores = (codigo, nombre, estado, id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tipo de documento actualizado con éxito.")


# Función para borrar un tipo de documento por su id
def borrar_tipo_documento(id):
    sql = "DELETE FROM tipodocumento WHERE id = %s"
    valores = (id,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tipo de documento eliminado con éxito.")


# Ejemplo de uso
crear_tipo_documento("DNI", "Documento Nacional de Identidad", "Activo")
leer_tipos_documentos()
actualizar_tipo_documento(3, "DNI", "Documento Nacional de Identidad", "Inactivo")
leer_tipos_documentos()
borrar_tipo_documento(2)
leer_tipos_documentos()

# Cerrar cursor y conexión
cursor.close()
conexion.close()
