# En linux se debe instalar: sudo apt install python3-tk

import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primer programa Tkinter")
ventana.geometry("500x300")
ventana.config(cursor="Hand2")

fuente = ("Roboto",36,"bold")

etiqueta = tk.Label(text="¡Hola Mundo!",bg="lightgreen", fg="red",borderwidth=25,cursor="hand2",state=tk.DISABLED,disabledforeground="sky blue",font=fuente)
etiqueta.pack()

boton = tk.Button(text="Haz click",font=fuente,bg="green2",foreground="deep pink",activeforeground="white",activebackground="blue",borderwidth=5,cursor="cross")
boton.pack()

entrada = tk.Entry(ventana,background="tomato",foreground="DarkOrange1")
entrada.config(bd=1,relief="solid",cursor="xterm")
entrada.pack()

texto = tk.Text(ventana)
texto.config(background="tan1",font=("Calibri",14),foreground="DarkOliveGreen4",cursor="pencil",width=25,height=10)
texto.pack()

ventana.mainloop()

# ME QUEDE EN 1 HORA.

