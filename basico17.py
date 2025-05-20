import tkinter as tk
from tkinter import ttk 

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("700x400")

etiqueta = ttk.Label(ventana,text="Esto es ttk",font=("Helvetica",15)).pack(pady=10)

boton = ttk.Button(ventana, text="Aceptar").pack()

style = ttk.Style()
style.theme_use("vista")

boton2 = ttk.Button(ventana, text="Boton TTK").pack(pady=15)

ventana.mainloop()