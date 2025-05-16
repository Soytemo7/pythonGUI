
import tkinter as tk
import platform

def click(evento):
    print("Boton pulsado")
    etiqueta.config(text="Boton pulsado")

def mover(evento):   
    x,y = evento.x,evento.y
    etiqueta2.config(text=f"Posicion del cursor: x={x}, y={y}")

def entrar(evento):
    etiqueta3.config(bg="red")

def salir(evento):
    etiqueta3.config(bg="white")

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

boton = tk.Button(ventana, text="Haz click")
boton.pack()
boton.bind("<Button>",click)

etiqueta = tk.Label(ventana,text="Boton no pulsado")
etiqueta.pack()

ventana.bind("<Motion>",mover)
etiqueta2 = tk.Label(ventana, text="Mueve el cursor")
etiqueta2.pack()

etiqueta3 = tk.Label(ventana,text="Pase el cursor sobre esta etiqueta")
etiqueta3.pack(pady=20)
etiqueta3.bind("<Enter>",entrar)
etiqueta3.bind("<Leave>",salir)

sistema_operativo =platform.system()
etiqueta4 = tk.Label(ventana,text=sistema_operativo)
etiqueta4.pack(pady=20)

ventana.mainloop()
