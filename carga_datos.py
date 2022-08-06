import tkinter


def guardar():
    nombre = t_nombre.get()
    t_nombre.delete(0,tkinter.END)
    apellido = t_apellido.get()
    t_apellido.delete(0,tkinter.END)
    dni = t_dni.get()
    t_dni.delete(0,tkinter.END)
    lista.append((nombre,apellido,dni))
    t_nombre.focus()
    l_lista.insert(0,(nombre,apellido,dni))
    print(lista)

def obtener(i):
    nombre = lista[i][0]
    apellido = lista[i][1]
    dni = lista[i][2]
    t_nombre.delete(0,tkinter.END)
    t_apellido.delete(0,tkinter.END)
    t_dni.delete(0,tkinter.END)
    t_nombre.insert(0,nombre)
    t_apellido.insert(0,apellido)
    t_dni.insert(0,dni)
    


lista = []
a = 0
ventana = tkinter.Tk()
t_nombre = tkinter.Entry(ventana)
t_apellido = tkinter.Entry(ventana)
t_dni = tkinter.Entry(ventana)
b_guardar = tkinter.Button(ventana, text="Guardar", command = guardar)
b_obtener = tkinter.Button(ventana, text="Obtner", command = lambda: obtener(a))
l_lista = tkinter.Listbox()
t_nombre.pack()
t_apellido.pack()
t_dni.pack()
l_lista.pack()
b_guardar.pack(side=tkinter.LEFT)
b_obtener. pack(side=tkinter.RIGHT)

ventana.mainloop()
