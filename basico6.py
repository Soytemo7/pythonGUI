 
import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

elemento_1 = tk.Label(ventana,text="Elemento 1",bg="gold")
elemento_2 = tk.Label(ventana,text="Elemento 2",bg="lightblue")
elemento_3 = tk.Label(ventana,text="Elemento 3",bg="lightgreen")
elemento_4 = tk.Label(ventana,text="Elemento 4",bg="lightpink")
elemento_5 = tk.Label(ventana,text="Elemento 5",bg="lightpink")

elemento_1.grid(row=0,column=0,columnspan=2,sticky="we")
elemento_2.grid(row=0,column=2)
elemento_3.grid(row=1,column=0)
elemento_4.grid(row=1,column=1,rowspan=2,sticky="ns")
elemento_5.grid(row=2,column=0)

ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=2)
ventana.rowconfigure(2,weight=1)

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=2)

ventana.mainloop()

# 3 HORAS 1 MINUTO.