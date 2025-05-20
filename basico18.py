# https://wiki.tcl-lang.org/page/List+of+ttk+Themes
# https://github.com/thindil/tkBreeze
# pip install ttkthemes

import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk

root = ThemedTk()
root.tk.call("source","./pythongui/breeze-dark/breeze-dark.tcl")

root.set_theme("breeze-dark")

root.geometry("400x300")
root.title("Ventana con tema Breeze Dark")

label = ttk.Label(root,text="Etiqueta con tema",font=("Arial",14)).pack(pady=20)

entry = ttk.Entry(root,width=30).pack(pady=10)

button = ttk.Button(root,text="Boton con tema").pack(pady=10)

def reaccionar(evento):
    seleccion = combo.get()
    print("Elegiste",seleccion)

combo = ttk.Combobox(root, values=["A","B","C"],state="reaadonly")
combo.pack(pady=10)
combo.current(0)
combo.bind("<<ComboboxSelected>>",reaccionar)

progress = ttk.Progressbar(root,length=200,mode="indeterminate")
progress.pack(pady=20)
progress.start()

root.mainloop()


# 6:00:03

