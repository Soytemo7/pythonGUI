import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

def tecla(evento):
    print(f"Tecla presionada {evento.keysym}")
    print(f"Tecla presionado {evento.keycode}")

def guardar(evento):
    print(f"Se guardaron los cambios {evento.keysym}")

def al_presionar(evento):
    print(f"Se presiono la tecla: {evento.keysym}")

def al_soltar(evento):
    print(f"Se solto la tecla: {evento.keysym}")

def foco_activo(evento):
    etiqueta.config(text="Foco activo en el boton")

def foco_inactivo(evento):
    etiqueta.config(text="Foco inactivo en el boton")

def actualizar_tamano(evento):
    ancho = evento.width
    alto = evento.height

    etiqueta2.config(text=f"Tamaño: {ancho}x{alto}")

ventana.bind("<KeyPress>",tecla)
ventana.bind("<Control-s>",guardar)
ventana.bind("<KeyPress>",al_presionar)
ventana.bind("<KeyRelease>",al_soltar)

entrada = tk.Entry(ventana)
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Presiona aqui")
boton.pack(pady=20)

etiqueta = tk.Label(ventana,text="Coloca el foco en el boton para ver el estado")
etiqueta.pack(pady=20)

boton.bind("<FocusIn>",foco_activo)
boton.bind("<FocusOut>",foco_inactivo)

etiqueta2 = tk.Label(ventana,text="Tamaño: 500x500")
etiqueta2.pack(expand=True,fill="both")

ventana.bind("<Configure>",actualizar_tamano)

etiqueta3 = tk.Label(ventana,text="",font=("Arial",16))
etiqueta3.pack(pady=20)

def saludar():
    etiqueta3.config(text="Hola usuario")

ventana.after(3000,saludar)


contador = 1

def verificar_foco():
    global contador
    if not ventana.focus_displayof():
        print(f"La ventana no tiene foco. Mensaje # {contador}")
    
    ventana.after_idle(verificar_foco)


ventana.after(100,verificar_foco)

nombre_var = tk.StringVar()
tk.Label(ventana, text="Escribe tu nombre").pack()

entrada2 = tk.Entry(ventana,textvariable=nombre_var)
entrada2.pack()

etiqueta4 = tk.Label(ventana,textvariable=nombre_var) 
etiqueta4.pack()

ventana.mainloop()
