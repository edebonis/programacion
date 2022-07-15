import tkinter
from functools import partial

def borrar(i,j):
    print(i,j)
    x = i
    y = j
    if tablero[i][j].cget("relief") != tkinter.SUNKEN:
        tablero[i][j].config(relief=tkinter.SUNKEN, text = "*")
        for fila in range(8):
            tablero[fila][j].config(relief=tkinter.SUNKEN)
        for columna in range(8):
            tablero[i][columna].config(relief=tkinter.SUNKEN)
        while x>=0 and y>=0:
            tablero[x][y].config(relief=tkinter.SUNKEN)
            x-=1
            y-=1
        x = i
        y = j
        while x<8 and y<8:
            tablero[x][y].config(relief=tkinter.SUNKEN)
            x+=1
            y+=1
        x = i
        y = j
        while x<8 and y>=0:
            tablero[x][y].config(relief=tkinter.SUNKEN)
            x+=1
            y-=1
        x = i
        y = j
        while y<8 and x>=0:
            tablero[x][y].config(relief=tkinter.SUNKEN)
            x-=1
            y+=1
v = tkinter.Tk()
tablero = []
for i in range(8):
    lista = []
    for j in range(8):
        b = tkinter.Button(v, height=2, width=2, command=partial(borrar, i, j))
        lista.append(b)
        b.grid(row=i, column=j)
    tablero.append(lista)

v.mainloop()