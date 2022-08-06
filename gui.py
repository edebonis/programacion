import tkinter
from tkinter import ttk, messagebox
from functools import partial
from screeninfo import get_monitors
from datetime import datetime, date

h = get_monitors()[0].height
w = get_monitors()[0].width

def saludar(ventana):
    today = date.today().strftime(" %d/%m/%Y")
    ventana.title(today)
    

    
ventana = tkinter.Tk()
ventana.title("Nombre")
ventana.geometry('{}x{}+{}+{}'.format(w//2,h//2,(w-w//2)//2,(h-h//2)//2))

boton = ttk.Button(text="¡Hola, mundo!", command = lambda: saludar(ventana))
boton.place(x=50, y=50)


ventana.mainloop()
