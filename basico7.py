 
import tkinter as tk

ventana =tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

elemento_1 = tk.Label(ventana, text="Elemento 1", bg="gold")
elemento_2 = tk.Label(ventana, text="Elemento 2", bg="lightblue")
elemento_3 = tk.Label(ventana, text="Elemento 3", bg="lightgreen")
elemento_4 = tk.Label(ventana, text="Elemento 4", bg="lightpink")

# elemento_1.place(x=0,y=0,width=160,height=50)
# elemento_2.place(x=170,y=0,width=160,height=50)
# elemento_3.place(x=0,y=60,width=160,height=50)
# elemento_4.place(x=170,y=60,width=160,height=50)

elemento_1.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
elemento_2.place(relx=0.30, rely=0, relwidth=0.25, relheight=0.25)
elemento_3.place(relx=0, rely=0.30, relwidth=0.25, relheight=0.25)
elemento_4.place(relx=0.30, rely=0.30, relwidth=0.25, relheight=0.55)

ventana.mainloop()