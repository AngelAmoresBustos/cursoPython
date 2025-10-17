from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

# Configuración (puedes usar variables de entorno)
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "127.0.0.1"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASS", ""),
    "database": os.environ.get("DB_NAME", "pruebas"),
    "port": int(os.environ.get("DB_PORT", 3306)),
    "charset": "utf8mb4"
}

app = Flask(__name__)
CORS(app)  # permite llamadas desde la GUI local u otros orígenes

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/tipos-documento", methods=["POST"])
def crear_tipo_documento():
    data = request.get_json() or {}
    codigo = data.get("codigo")
    nombre = data.get("nombre")
    estado = data.get("estado", "Activo")

    if not codigo or not nombre:
        return jsonify({"error": "codigo y nombre son obligatorios"}), 400

    conn = get_connection()
    try:
        cur = conn.cursor()
        sql = "INSERT INTO tipodocumento (codigo, nombre, estado) VALUES (%s, %s, %s)"
        cur.execute(sql, (codigo, nombre, estado))
        conn.commit()
        nuevo_id = cur.lastrowid
        cur.close()
        return jsonify({"mensaje": "creado", "id": nuevo_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route("/tipos-documento", methods=["GET"])
def listar_tipos_documento():
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, codigo, nombre, estado FROM tipodocumento")
        rows = cur.fetchall()
        cur.close()
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route("/tipos-documento/<int:doc_id>", methods=["PUT"])
def actualizar_tipo_documento(doc_id):
    data = request.get_json() or {}
    codigo = data.get("codigo")
    nombre = data.get("nombre")
    estado = data.get("estado")

    if not any([codigo, nombre, estado]):
        return jsonify({"error": "Al menos un campo debe ser provisto para actualizar"}), 400

    conn = get_connection()
    try:
        cur = conn.cursor()
        # Construir actualización dinámica segura
        campos = []
        valores = []
        if codigo is not None:
            campos.append("codigo = %s")
            valores.append(codigo)
        if nombre is not None:
            campos.append("nombre = %s")
            valores.append(nombre)
        if estado is not None:
            campos.append("estado = %s")
            valores.append(estado)
        valores.append(doc_id)
        sql = f"UPDATE tipodocumento SET {', '.join(campos)} WHERE id = %s"
        cur.execute(sql, tuple(valores))
        conn.commit()
        cur.close()
        return jsonify({"mensaje": "actualizado", "filas_afectadas": cur.rowcount}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route("/tipos-documento/<int:doc_id>", methods=["DELETE"])
def eliminar_tipo_documento(doc_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM tipodocumento WHERE id = %s", (doc_id,))
        conn.commit()
        filas = cur.rowcount
        cur.close()
        if filas == 0:
            return jsonify({"mensaje": "no existe el id"}), 404
        return jsonify({"mensaje": "eliminado", "filas_afectadas": filas}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
