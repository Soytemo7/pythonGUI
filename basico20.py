import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("700x400")

def abrir():
    print("Abrir Archivo")

def guardar():
    print("Guardar Archivo")

def salir():
    ventana.quit()

barra_menu = tk.Menu(ventana)
menu_archivo = tk.Menu(barra_menu,tearoff=0)

menu_archivo.add_command(label="Abrir",command=abrir, accelerator="Ctrl+O")
menu_archivo.add_command(label="Guardar",command=guardar, accelerator="Ctrl+S")
menu_archivo.add_command(label="Salir",command=salir, accelerator="Ctrl+Q")

ventana.bind("<Control-o>",lambda event: abrir())
ventana.bind("<Control-s>",lambda event: guardar())
ventana.bind("<Control-q>",lambda event: salir())

barra_menu.add_cascade(label="Archivo",menu=menu_archivo)

ventana.config(menu=barra_menu)

ventana.mainloop()

