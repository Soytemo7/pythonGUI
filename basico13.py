
import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

def etiqueta_seleccion():
    tk.Label(ventana, text=variable_control.get()).pack()

variable_control = tk.IntVar()

confirmacion_1 = tk.Checkbutton(ventana,text="Opcion 1",variable=variable_control)
confirmacion_1.pack()

muestra_seleccion = tk.Button(ventana,text="Mostrar seleccion",command=etiqueta_seleccion).pack()

ventana.mainloop()

#ME QUEDE EN 5 HORAS 10 MINUTOS.