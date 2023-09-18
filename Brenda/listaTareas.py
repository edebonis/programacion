import tkinter as tk
from tkinter import ttk
from datetime import datetime

def guardar():
    today = datetime.today()
    fecha = f"{today.day}/{today.month}/{today.year}"
    treeview.insert(
    "",
    tk.END,
    text=texto.get(),
    values=(fecha, False)
)

main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview(columns=("fecha", "completada"))
treeview.heading("#0", text="Tarea")
treeview.heading("fecha", text="Fecha")
treeview.heading("completada", text="Completada")

treeview.pack()

texto = tk.Entry(main_window)
texto.pack()
btn = tk.Button(main_window, text="Guardar", command=guardar)
btn.pack()
main_window.mainloop()