import tkinter as tk
from tkinter import ttk, messagebox
import requests

# URL base del endpoint Flask (ajústala según tu entorno)
API_URL = "http://127.0.0.1:5000/tipos-documento"


class AppCRUD(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Tipo de Documento")
        self.geometry("650x450")
        self.resizable(False, False)

        # --- MENÚ SUPERIOR ---
        menu_bar = tk.Menu(self)
        crud_menu = tk.Menu(menu_bar, tearoff=0)
        crud_menu.add_command(label="Crear", command=self.crear)
        crud_menu.add_command(label="Leer", command=self.leer)
        crud_menu.add_command(label="Actualizar", command=self.actualizar)
        crud_menu.add_command(label="Eliminar", command=self.eliminar)
        crud_menu.add_command(label="Limpiar", command=self.limpiar)
        crud_menu.add_separator()
        crud_menu.add_command(label="Salir", command=self.salir)
        menu_bar.add_cascade(label="Operaciones CRUD", menu=crud_menu)
        self.config(menu=menu_bar)

        # --- ZONA DE CAMPOS ---
        frame_campos = tk.LabelFrame(self, text="Datos del Tipo de Documento", padx=10, pady=10)
        frame_campos.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_campos, text="ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(frame_campos, text="Código:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(frame_campos, text="Nombre:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Label(frame_campos, text="Estado:").grid(row=3, column=0, sticky="e", padx=5, pady=5)

        self.entry_id = tk.Entry(frame_campos, width=40)
        self.entry_codigo = tk.Entry(frame_campos, width=40)
        self.entry_nombre = tk.Entry(frame_campos, width=40)
        self.entry_estado = tk.Entry(frame_campos, width=40)

        self.entry_id.grid(row=0, column=1, pady=5)
        self.entry_codigo.grid(row=1, column=1, pady=5)
        self.entry_nombre.grid(row=2, column=1, pady=5)
        self.entry_estado.grid(row=3, column=1, pady=5)

        # --- TABLA DE RESULTADOS ---
        frame_tabla = tk.Frame(self)
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        self.tabla = ttk.Treeview(frame_tabla, columns=("ID", "Código", "Nombre", "Estado"), show='headings', height=10)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Código", text="Código")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Estado", text="Estado")
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_registro)

        for col in ("ID", "Código", "Nombre", "Estado"):
            self.tabla.column(col, width=140, anchor="center")

        self.tabla.pack(side="left", fill="both", expand=True)

        scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right", fill="y")

        # --- BOTONES INFERIORES ---
        frame_botones = tk.Frame(self)
        frame_botones.pack(side="bottom", pady=5)

        tk.Button(frame_botones, text="Crear", width=12, bg="green", command=self.crear).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Leer", width=12, bg="blue", command=self.leer).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Actualizar", width=12, bg="yellow", command=self.actualizar).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Eliminar", width=12, bg="red", command=self.eliminar).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Limpiar", width=12, bg="white", command=self.limpiar).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Salir", width=12, bg="black", fg="white", command=self.salir).pack(side="left", padx=5)


    def seleccionar_registro(self, event):
        try:
            # Obtener el elemento seleccionado
            item = self.tabla.focus()
            if not item:
                return
            valores = self.tabla.item(item, 'values')

            # Llenar los campos (ajusta los nombres según tu código)
            self.entry_id.delete(0, tk.END)
            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_estado.delete(0, tk.END)

            self.entry_id.insert(0, valores[0])
            self.entry_codigo.insert(0, valores[1])
            self.entry_nombre.insert(0, valores[2])
            self.entry_estado.insert(0, valores[3])

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear. Código {e}")

    # --- FUNCIONES CRUD ---
    def crear(self):
        datos = {
            "codigo": self.entry_codigo.get(),
            "nombre": self.entry_nombre.get(),
            "estado": self.entry_estado.get()
        }
        if not datos["codigo"] or not datos["nombre"]:
            messagebox.showwarning("Atención", "Código y Nombre son obligatorios.")
            return
        
        try:
            response = requests.post(API_URL, json=datos)
            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Registro creado correctamente.")
                self.leer()
            else:
                messagebox.showerror("Error", f"No se pudo crear. Código {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def leer(self):
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                registros = response.json()
                for row in self.tabla.get_children():
                    self.tabla.delete(row)
                for reg in registros:
                    self.tabla.insert("", "end", values=(reg['id'], reg['codigo'], reg['nombre'], reg['estado']))
            else:
                messagebox.showerror("Error", "No se pudo obtener los registros.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def actualizar(self):
        id_doc = self.entry_id.get()
        if not id_doc:
            messagebox.showwarning("Atención", "Debe ingresar un ID para actualizar.")
            return
        datos = {
            "codigo": self.entry_codigo.get(),
            "nombre": self.entry_nombre.get(),
            "estado": self.entry_estado.get()
        }
        try:
            response = requests.put(f"{API_URL}/{id_doc}", json=datos)
            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
                self.leer()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el registro.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def eliminar(self):
        res=messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este registro?")
        if not res:
            return
        
        id_doc = self.entry_id.get()
        if not id_doc:
            messagebox.showwarning("Atención", "Debe ingresar un ID para eliminar.")
            return
        
        try:
            response = requests.delete(f"{API_URL}/{id_doc}")
            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
                self.leer()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def limpiar(self):
        try:
            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_estado.delete(0, tk.END)
            self.entry_id.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            messagebox.showinfo("Exito", "Campos limpiados.")


    def salir(self):
        self.destroy()


# --- EJECUTAR APLICACIÓN ---
if __name__ == "__main__":
    app = AppCRUD()
    app.mainloop()
