import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

opcion = tk.IntVar()
opcion.set(1)

def actualiza_radio(valor):
    tk.Label(ventana,text=valor).pack()

def actualiza_radio2():
    valor = opcion.get()
    etiqueta_resultado.config(text=f"Opcion Seleccionada: {valor}")

opcion1 = tk.Radiobutton(ventana,text="Opcion 1",variable=opcion,value=1, command=actualiza_radio2)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana,text="Opcion 2",variable=opcion,value=2, command=actualiza_radio2)
opcion2.pack()

boton_enviar = tk.Button(ventana,text="Enviar", command=lambda: actualiza_radio(opcion.get())).pack()

etiqueta_resultado = tk.Label(ventana, text="Selecciona una opcion")
etiqueta_resultado.pack()



ventana.mainloop()