
# 🐍 CURSO DE PYTHON - Una colección de ejercicios de aprendizaje de Python para principiantes
# Para hacer interesante se hizo un CRUD que es la parte cuspide de este mini curso.
# CRUD de Tipos de Documento — Python + Flask + Tkinter + MySQL

Este proyecto es un **ejercicio práctico completo** de desarrollo en Python que integra:

- **Backend REST API** con Flask  
- **Base de datos MySQL**  
- **Interfaz gráfica (GUI)** en Tkinter  
- **Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar)**  

El objetivo es mostrar cómo crear un sistema básico de gestión (CRUD) con conexión a base de datos y una interfaz amigable.

---

## 📁 Estructura del Proyecto

```
flask_api/
│
├── app.py                # Endpoint Flask (API REST)
├── requirements.txt      # Dependencias del backend
└── .env (opcional)       # Variables de entorno para conexión MySQL
crud_gui.py               # Aplicación gráfica (Tkinter)
*.py                      # Todos los ejercicios
README.md                 # Este archivo
```

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

- **Python 3.8 o superior**
- **MySQL Server** (o MariaDB)
- **pip** (administrador de paquetes de Python)

---

## 🧱 1. Configurar la base de datos MySQL

Conéctate a tu servidor MySQL y ejecuta:

```sql
CREATE DATABASE IF NOT EXISTS pruebas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE pruebas;

CREATE TABLE IF NOT EXISTS tipodocumento (
  id INT AUTO_INCREMENT PRIMARY KEY,
  codigo VARCHAR(50) NOT NULL,
  nombre VARCHAR(255) NOT NULL,
  estado VARCHAR(50) DEFAULT 'Activo'
);
```

---

## 🧩 2. Crear el entorno virtual e instalar dependencias

En la raíz del proyecto:

```bash
python -m venv venv
# Activar entorno virtual
# Windows:
.env\Scriptsctivate
# Linux / macOS:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

Contenido de `requirements.txt`:
```
Flask>=2.0
mysql-connector-python>=8.0
Flask-Cors>=3.0
requests>=2.0
```

---

## 🚀 3. Ejecutar el Endpoint (API Flask)

El archivo principal del backend es `app.py`.  
Ejecuta el servidor con:

```bash
python app.py
```

Por defecto el API se inicia en:
```
http://127.0.0.1:5000
```

### Endpoints disponibles:

| Método | Endpoint | Descripción |
|---------|-----------|-------------|
| `GET` | `/tipos-documento` | Lista todos los tipos de documento |
| `POST` | `/tipos-documento` | Crea un nuevo registro |
| `PUT` | `/tipos-documento/<id>` | Actualiza un registro existente |
| `DELETE` | `/tipos-documento/<id>` | Elimina un registro |

Ejemplo `POST`:
```bash
curl -X POST http://127.0.0.1:5000/tipos-documento   -H "Content-Type: application/json"   -d '{"codigo":"DOC01", "nombre":"Documento de Identidad", "estado":"Activo"}'
```

---

## 🖥️ 4. Ejecutar la aplicación gráfica (Tkinter)

El archivo `gui_app.py` contiene la interfaz visual.  
Ejecuta:

```bash
python gui_app.py
```

### Características de la GUI:
- Menú superior con opciones CRUD  
- Campos editables para cada atributo de la tabla (`id`, `codigo`, `nombre`, `estado`)  
- Tabla (Treeview) con todos los registros  
- Botones inferiores para Crear, Actualizar, Eliminar, Limpiar, y Salir  
- Al hacer clic en una fila, los valores se cargan automáticamente en los campos de entrada  
- Conexión directa al endpoint Flask usando el método `POST`  

---

## 🧠 Flujo de funcionamiento

1. La API Flask se conecta a la base de datos `pruebas`.
2. La app gráfica envía y recibe datos mediante peticiones HTTP (usando `requests`).
3. Las operaciones CRUD se ejecutan de forma remota y los resultados se reflejan en la interfaz.

---

## 🧰 5. Variables de entorno (opcional)

Puedes configurar credenciales seguras para MySQL:

```bash
# Windows (cmd)
set DB_HOST=127.0.0.1
set DB_USER=root
set DB_PASS=tu_password
set DB_NAME=pruebas

# Linux / macOS
export DB_HOST=127.0.0.1
export DB_USER=root
export DB_PASS=tu_password
export DB_NAME=pruebas
```

Si no las configuras, `app.py` usará los valores por defecto.

---

## 🧹 6. Cierre de la aplicación

Para salir de la interfaz gráfica:
```python
root.destroy()
```
También hay un botón **Salir** en la parte inferior del programa.

---

## 🧩 7. Tecnologías utilizadas

| Componente  | Tecnología  |
|-------------|-------------|
| Lenguaje    | Python 3    |
| Backend     | Flask       |
| BBDD        | MySQL       |
| Cliente GUI | Tkinter     |
| API Client  | requests    |
| Conexión DB | mysql-conn  |
---


## 👨‍💻 Autor

**Angel Amores**  
Software Engineer — apasionado por la tecnología, la automatización y la inteligencia artificial.  
💡 *“Utilizar software es humano, crearlo es divino.”*

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.  
Puedes usarlo, modificarlo y compartirlo libremente, citando la fuente.

---
