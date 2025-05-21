import tkinter as tk

root = tk.Tk()
root.title("Mostrar imagen con Tkinter")
root.geometry("500x500")

icono = tk.PhotoImage(file="pythongui/img/favicon-32x32.png")

root.iconphoto(False,icono)

root.mainloop()
