from pathlib import Path
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def abrir():
    # Intentar argumento de línea de comandos
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        if p.is_file():
            return str(p.resolve())

    # Abrir diálogo de selección de archivo
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    filetypes = [("PDF files", "*.pdf"), ("All files", "*.*")]
    filename = askopenfilename(title="Selecciona un archivo PDF", filetypes=filetypes)
    root.destroy()
    return filename


miArchivo=abrir()

if miArchivo:
    print("Archivo seleccionado:", miArchivo)
else:
    print("No se seleccionó ningún archivo.")