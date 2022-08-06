import tkinter as tk
from itertools import cycle
from PIL import ImageTk, Image
import random

root = tk.Tk()
images = []
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)


def slideShow():
    ind = random.randint(0,5)
    for i in range(0,ind):
        img = next(photos)
    
    displayCanvas.config(image=img)
    #root.after(1000, slideShow)


#root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenwidth()
#root.geometry('%dx%d' % (640, 480))
displayCanvas = tk.Label(root)
displayCanvas.pack()
boton = tk.Button(root, text="otra", command= lambda: slideShow())
boton.pack()
root.mainloop()