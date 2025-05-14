import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

boton_1 = tk.Button(ventana,text="Noroeste").pack(anchor=tk.NW)
boton_2 = tk.Button(ventana,text="Norte").pack(anchor=tk.N)
boton_3 = tk.Button(ventana,text="Noreste").pack(anchor=tk.NE)
boton_4 = tk.Button(ventana,text="Oeste").pack(anchor=tk.W)
boton_5 = tk.Button(ventana,text="Centre").pack(anchor=tk.CENTER)
boton_6 = tk.Button(ventana,text="Este").pack(anchor=tk.E)
boton_7 = tk.Button(ventana,text="Suroeste").pack(anchor=tk.SW)
boton_8 = tk.Button(ventana,text="Sur").pack(anchor=tk.S)
boton_9 = tk.Button(ventana,text="Sureste").pack(anchor=tk.SE)

buton_10 = tk.Button(ventana,text="Soy el boton 10",bg="deep pink")
buton_11 = tk.Button(ventana,text="Soy el boton 11",bg="SpringGreen")
buton_12 = tk.Button(ventana,text="Soy el boton 12",bg="SpringGreen")
buton_13 = tk.Button(ventana,text="Soy el boton 13",bg="SpringGreen")

buton_10.pack(expand=True,fill="both")
buton_11.pack(before=buton_10,fill="x")
buton_12.pack(side="right")
buton_13.pack(side=tk.LEFT)

etiqueta_1 = tk.Label(ventana,text="Etiqueta expansible",bg="SpringGreen",padx=100,pady=50)
etiqueta_1.pack(padx=10,pady=10,ipadx=10,ipady=10)

ventana.mainloop()

