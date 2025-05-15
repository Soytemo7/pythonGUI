
import tkinter as tk

ventana =tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")


scrollbar_v = tk.Scrollbar(ventana)
scrollbar_v.pack(side="right",fill="y")

scrollbar_h2 = tk.Scrollbar(ventana,orient="horizontal")
scrollbar_h2.pack(side="bottom",fill="x")

lista = tk.Listbox(ventana, selectmode=tk.EXTENDED,yscrollcommand=scrollbar_v.set,xscrollcommand=scrollbar_h2.set)
lista.pack(pady=10,side="left",fill="both",expand=True)

elementos = ["Rojooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo","Azul","Verde"]

# lista.insert(0,"Elemento 1")
# lista.insert(1,"Elemento 2")
# lista.insert(2,"Elemento 3")

lista.insert(0,*elementos)

elementos_tamaño = lista.size()
print(f"La lista contiene {elementos_tamaño} elementos.")

elemento_1 = lista.get(1)
print(f"El elemento es: {elemento_1}")

elemento_2 = lista.delete(2)
print(f"El elemento es: {elementos}")

for i in range(1,51):
    lista.insert(tk.END, f"Elemento No. {i}")

lista.see(25)
lista.itemconfigure(27,selectbackground="blue",selectforeground="white",bg="green")

scrollbar_v.config(command=lista.yview)
scrollbar_h2.config(command=lista.xview)

def mostrar_seleccion():
    seleccion = lista.curselection()
    elementos_seleccionados = [lista.get(i) for i in seleccion]
    print("Elementos seleccionados: ",elementos_seleccionados)

lista.bind("<<ListboxSelect>>",lambda evento:mostrar_seleccion())

# SCROLL

scrollbar = tk.Scrollbar(ventana)
scrollbar_h = tk.Scrollbar(ventana,orient="horizontal")

scrollbar.pack(side="right",fill="y")
scrollbar_h.pack(side="bottom",fill="x")

texto = tk.Text(ventana,yscrollcommand=scrollbar.set)
texto.pack(side="left",fill="both",expand=True)

scrollbar.config(command=texto.yview)

ventana.mainloop()