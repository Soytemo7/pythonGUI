import tkinter as tk

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("700x400")

barra_menu = tk.Menu(ventana)

menu_archivo = tk.Menu(barra_menu,tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.entryconfig("Guardar",state="disabled")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir")

menu_exportar =tk.Menu(menu_archivo,tearoff=0)
menu_exportar.add_command(label="Como PDF", command=lambda: print("Exportar a PDF"))
menu_exportar.add_command(label="Como Imagen", command=lambda: print("Exportar a Imagen"))

menu_editar = tk.Menu(barra_menu,tearoff=0)
menu_editar.add_command(label="Deshacer")
menu_editar.add_command(label="Rehacer")

mostrar_toolbar = tk.BooleanVar()
mostrar_estado = tk.BooleanVar(value=True)

tema_color =tk.StringVar(value="claro")

menu_ver = tk.Menu(barra_menu,tearoff=0)
menu_ver.add_checkbutton(label="Mostrar barra de herramientas", variable=mostrar_toolbar)
menu_ver.add_checkbutton(label="Mostrar barra de estado", variable=mostrar_estado)

menu_tema = tk.Menu(barra_menu,tearoff=0)
menu_tema.add_radiobutton(label="Claro",variable=tema_color,value="claro")
menu_tema.add_radiobutton(label="Oscuro",variable=tema_color,value="oscuro")

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Editar", menu=menu_editar)
barra_menu.add_cascade(label="Ver", menu=menu_ver)
barra_menu.add_cascade(label="Tema",menu=menu_tema)

menu_archivo.add_cascade(label="Exportar", menu=menu_exportar)

ventana.config(menu=barra_menu)

def activar_guardar():
    menu_archivo.entryconfig("Guardar",state="normal")


def elegir_color(color):
    print(f"Color seleccionado: {color}")

menu_colores = tk.Menu(barra_menu,tearoff=0)
menu_colores.add_command(label="Rojo", command=lambda: elegir_color("Rojo"))
menu_colores.add_command(label="Azul", command=lambda: elegir_color("Azul"))
menu_colores.add_command(label="Verde", command=lambda: elegir_color("Verde"))

barra_menu.add_cascade(label="Color",menu=menu_colores)

boton_activar = tk.Button(ventana,text="Activar Guardar",command=activar_guardar)
boton_activar.pack(pady=20)

ventana.mainloop()
