import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Abre un archivo",initialdir=".",filetypes=[("Archivos de texto","*.txt"),("Todos los archivos","*.*")])
    if archivo:
        print("Archivo seleccionado: ",archivo)

def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(title="Abre archivos",initialdir=".",filetypes=[("Archivos de python","*.py"),("Todos los archivos","*.*")])
    if archivos:
        print("Archivo seleccionado: ")
        for archivo in archivos:
            print(archivo)

def guardar_como():
    archivo = filedialog.asksaveasfilename(title="Guardar como",defaultextension=".txt",filetypes=[("Archivos de texto","*.txt"),("Todos los archivos","*.*")])
    if archivo:
        print("Guardar en: ",archivo)

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory(title="Seleccione carpeta")
    if carpeta:
        print("Carpeta seleccionada: ",carpeta)

boton = tk.Button(ventana,text="Seleccionar Archivo",command=seleccionar_archivo)
boton.pack(pady=20)

boton2 = tk.Button(ventana,text="Seleccionar Archivos",command=seleccionar_archivos)
boton2.pack(pady=20)

boton3 = tk.Button(ventana,text="Seleccionar Archivos",command=guardar_como)
boton3.pack(pady=20)

boton4 = tk.Button(ventana,text="Seleccionar Carpeta",command=seleccionar_carpeta)
boton4.pack(pady=20)

ventana.mainloop()
