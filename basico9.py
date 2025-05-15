import tkinter as tk

def saludo():
    print("Hola")

def mostrar_info_evento(evento):
    print(f"Tipo de evento: {evento.type}")
    print(f"Widget: {evento.widget}")
    print(f"Char: {evento.char}")
    print(f"Keysim: {evento.keysym}")
    print(f"KeyCode: {evento.keycode}")
    print(f"Estado: {evento.state}")
    print(f"Raton X, Y: {evento.x}, {evento.y}")
    print(f"Screen X, Y: {evento.x_root}, {evento.y_root}")
    print(f"Tiempo: {evento.time}")
    print(f"Numero de Boton: {evento.num}")
    print(f"Delta: {evento.delta}")
    print("-"*20)    

ventana = tk.Tk()
ventana.geometry("550x500")

boton = tk.Button(ventana,text="Haz click aqui",command=saludo)
boton.pack()

ventana.bind("<KeyPress>",mostrar_info_evento)
ventana.bind("<ButtonPress>",mostrar_info_evento)
ventana.bind("<Motion>",mostrar_info_evento)
ventana.bind("<MouseWheel>",mostrar_info_evento)

ventana.mainloop()

