import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x300")

texto = tk.Text(ventana,width=50, height=15)
texto.pack()

contador = 0
def insertar_texto():
    global contador
    contador += 1
    texto.insert(tk.END,f"Linea {contador}\n")

boton_insertar = tk.Button(ventana, text="Insersar Texto",command=insertar_texto)
boton_insertar.pack()

ventana.mainloop()