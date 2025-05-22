import tkinter as tk
from tkinter import filedialog,messagebox

ventana = tk.Tk()
ventana.title("Python: Interfaces graficas")
ventana.geometry("500x500")

def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Abrir archivo de texto",initialdir=".",filetypes=[("Archivos de texto","*.txt")])
    if archivo:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()
                text_area.delete("1.0",tk.END)
                text_area.insert(tk.END,contenido)
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo abrir el archivo: \n{e}")

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(title="Guardar archivo de texto",defaultextension=".txt",filetypes=[("Archivos de texto","*.txt")])
    if archivo:
        try:
            with open(archivo,"w",encoding="utf-8") as f:
                contenido = text_area.get("1.0",tk.END).rstrip()
                f.write(contenido)
            messagebox.showinfo("Guardado","Archivo guardado correctamente")
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo guardar el archivo: \n{e}")

frame_texto = tk.Frame(ventana)
frame_texto.pack(expand=True, fill="both",padx=10,pady=10)

scroll_y = tk.Scrollbar(frame_texto,orient="vertical")
scroll_y.pack(side="right",fill="y")

text_area = tk.Text(frame_texto,wrap=tk.WORD,yscrollcommand=scroll_y.set)
text_area.pack(expand=True,fill="both")
scroll_y.config(command=text_area.yview)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_abrir = tk.Button(frame_botones,text="Abrir archivo",command=abrir_archivo)
btn_abrir.pack(side="left",padx=10)

btn_guardar = tk.Button(frame_botones, text="Guardar Archivo",command=guardar_archivo)
btn_guardar.pack(side="left",padx=10)

ventana.mainloop()
