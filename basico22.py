from operator import iadd
import tkinter as tk
# pip install Pillow
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Mostrar imagen con Tkinter")
root.geometry("500x500")

# https://www.iloveimg.com/es/convertir-a-jpg
imagen = tk.PhotoImage(file="pythongui/img/images.png")
# imagen = imagen.subsample(2,2)

pilimagen = Image.open("pythongui/img/images.jpg")
imagen_tk = ImageTk.PhotoImage(pilimagen)

label_imagen = tk.Label(root,image=imagen)
label_imagen.pack()

label_imagen2 = tk.Label(root,image=imagen_tk)
label_imagen2.pack()

root.mainloop()