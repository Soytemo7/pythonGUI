import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("550x500")

texto = tk.Text(ventana,width=50, height=15)
texto.pack()

texto.insert("1.0","Primera Linea\n")
texto.insert("2.0", "Segunda Linea\n")
texto.insert("3.0","Tercera Linea\n")

def eliminar_texto():
    texto.delete("1.0",tk.END)

def eliminar_texto_parcial():
    texto.delete("1.0","2.8")

def obtener_texto():
    texto_obtenido = texto.get("1.0","end")
    print(texto_obtenido)

def obtener_texto_parcial():
    texto_obtenido = texto.get("1.0","1.end")
    print(texto_obtenido)

def obtener_texto_seleccionado():
    seleccion = texto.get("sel.first","sel.last")
    print("Texto seleccionado: ", seleccion)

def modificar_seleccionado():
    nuevo_texto = "TEXTO MODIFICADO"
    texto.replace("sel.first","sel.last",nuevo_texto)    

def posicion_cursor(evento):
    posicion = texto.index(tk.INSERT)
    print("Posicion del cursor: ",posicion)

texto.bind("<KeyRelease>",posicion_cursor)

boton_eliminar = tk.Button(ventana, text="Eliminar texto",command=eliminar_texto)
boton_eliminar_parcial = tk.Button(ventana, text="Eliminar Parcial",command=eliminar_texto_parcial)
boton_obtener_texto = tk.Button(ventana,text="Obtener texto",command=obtener_texto)
boton_obtener_texto_parcial = tk.Button(ventana,text="Obtener texto parcial",command=obtener_texto_parcial)
boton_obtener_texto_seleccionado = tk.Button(ventana,text="Obtener texto seleccionado",command=obtener_texto_seleccionado)
boton_modificar_seleccionado = tk.Button(ventana,text="Modificar seleccionado",command=modificar_seleccionado)
boton_eliminar.pack()
boton_eliminar_parcial.pack()
boton_obtener_texto.pack()
boton_obtener_texto_parcial.pack()
boton_obtener_texto_seleccionado.pack()
boton_modificar_seleccionado.pack()

ventana.mainloop()