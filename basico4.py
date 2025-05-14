import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

print(f"Ancho de la pantalla: {ancho_pantalla} pixeles")
print(f"alto de la pantalla: {alto_pantalla} pixeles")

ancho_ventana= 500
alto_ventana=400

posicion_x = round(ancho_pantalla/2 - ancho_ventana/2)
posicion_y = round(alto_pantalla/ 2 - alto_ventana/2)

print(f"Posicion X para centrar la ventana: {posicion_x} pixeles")
print(f"Posicion Y para centrar la ventana: {posicion_y} pixeles")

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
ventana.resizable(True,True)

# ventana.wm_state("zoomed")

marco = tk.Frame(ventana)
marco.pack()
marco.config(bg="RoyalBlue",width=300,height=300,cursor="cross")

boton_1 = tk.Button(marco,text="Soy el primer boton")
boton_1.pack()
boton_2 = tk.Button(marco,text="Soy el segundo boton")
boton_2.pack()

ventana.mainloop()

# ME QUEDE EN: 2:03:00