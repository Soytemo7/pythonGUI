import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("700x400")

def mostrar_valor(valor):
    print("Valor seleccionado", valor)

var =tk.IntVar(value=5)
var2 = tk.StringVar()
scale = tk.Scale(ventana,from_=0,to=100,command=mostrar_valor,orient="horizontal",length=300,tickinterval=10,sliderlength=100,resolution=0.1).pack(fill="x")

lista = ["A","B","C"]
spin = tk.Spinbox(ventana, from_=0,to=10,increment=2,textvariable=var,wrap=True).pack()
spin2 = tk.Spinbox(ventana, values=("Opcion 1","Opcion 2","Opcion 3")).pack()
spin3 = tk.Spinbox(ventana, values=lista,textvariable=var2).pack()

def mostrar_valor():
    print("Valor seleccionado: ",var.get())

boton = tk.Button(ventana,text="Mostrar valor",command=mostrar_valor).pack()

def mostrar_valor2():
    print("Valor seleccionado: ",var2.get())

boton = tk.Button(ventana,text="Mostrar valor 2",command=mostrar_valor2).pack()

paned_window = tk.PanedWindow(ventana,orient="horizontal",bg="black")
paned_window.pack(fill=tk.BOTH,expand=True)

panel_izquierdo = tk.Frame(paned_window,bg="lightblue")
panel_derecho = tk.Frame(paned_window,bg="lightgreen")

paned_window.add(panel_izquierdo)
paned_window.add(panel_derecho)

paned_window.paneconfig(panel_izquierdo, stretch="always")
paned_window.paneconfig(panel_derecho, stretch="always")

ventana.mainloop()

