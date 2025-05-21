import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

def ir_configuracion():
    notebook.select(1)

def mostrar_pestana_actual():
    indice = notebook.index("current")
    print("Pestaña actual: ",indice)

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True,fill="both")

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1,text="Inicio")
notebook.add(tab2,text="Configuración")
notebook.add(tab3,text="Acerca de")

boton_cambiar = ttk.Button(tab1,text="Ir a configuracion",command=ir_configuracion)
boton_cambiar.pack()

boton_actual = ttk.Button(tab1, text="Mostrar pestaña actual",command=mostrar_pestana_actual)
boton_actual.pack()

ventana.mainloop()

# ME QUEDE EN 6:53:10