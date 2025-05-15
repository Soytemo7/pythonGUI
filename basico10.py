 
import tkinter as tk

def mouse_hover(evento):
    label_info.config(text="El raton ha estado sobre el widget por 5 segundos",background="red")

def iniciar_temporizador(evento):
    label_evento.after_id = label_evento.after(5000,lambda:label_evento.event_generate("<<EventoPersonalizado>>"))

def cancelar_temporizador(evento):
    if hasattr(label_evento,"after_id"):
        label_evento.after_cancel(label_evento.after_id)
        del label_evento.after_id

ventana = tk.Tk()
ventana.title("Python: Interfaces Graficas")

label_info = tk.Label(ventana,text="Pasa el raton sobre el widget y mantenlo por 5 segundos")
label_info.pack(padx=10,pady=10)

label_evento = tk.Label(ventana,text="Pasa el raton sobre mi")
label_evento.pack(padx=10,pady=10)

label_evento.bind("<Enter>",iniciar_temporizador)
label_evento.bind("<Leave>",cancelar_temporizador)
label_evento.bind("<<EventoPersonalizado>>",mouse_hover)

ventana.mainloop()

# ME QUEDE EN 4 HORAS 3 MINUTOS.