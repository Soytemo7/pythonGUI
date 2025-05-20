import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

messagebox.showinfo("Informacion","Es un mensaje informativo")
messagebox.showwarning("Informacion","Es un mensaje informativo")
messagebox.showerror("Informacion","Es un mensaje informativo")

respuesta= messagebox.askyesno("Confirmacion","¿Quieres Continuar?")
print(respuesta)

if respuesta:
    print("Se pulso el boton si")
else:
    print("Se pulso el boton no")

respuesta2= messagebox.askokcancel("Confirmacion","¿Quieres Salir?")
print(respuesta2)


respuesta3= messagebox.askretrycancel("Reintentar","¿Quieres Reintentar?")
print(respuesta3)

respuesta4= messagebox.askquestion("Reintentar","¿Quieres Continuar?")
print(respuesta4)

respuesta5= messagebox.askyesnocancel("Confirmacion","¿Quieres guardar?")
print(respuesta5)

ventana.mainloop()
