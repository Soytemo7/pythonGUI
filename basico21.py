import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("700x400")

ventana_secundaria = tk.Toplevel()
ventana_secundaria.title("Ventana Secundaria")
ventana_secundaria.geometry("300x200")

ventana_secundaria.configure(bg="lightblue")

tk.Label(ventana, text="Princiapal").pack()
tk.Label(ventana_secundaria, text="Princiapal").pack()

btn_cerrar =tk.Button(ventana,text="Cerrar Ventana",command=ventana_secundaria.destroy)
btn_cerrar.pack(pady=20)

sizegrip = ttk.Sizegrip(ventana)
sizegrip.place(relx=1.0,rely=1.0,anchor="se")

ventana.mainloop()