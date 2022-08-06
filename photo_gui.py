import tkinter as tk
from PIL import ImageTk, Image
import os
import json
import requests
from io import BytesIO
from PIL import Image,ImageTk

root = tk.Tk()
root.geometry("500x700")
img_url = "https://e00-marca.uecdn.es/assets/datos-deportivos/escudos/opta/png/128x128/608.png"
response = []
elementos = []
datos = requests.get("https://api.unidadeditorial.es/sports/v1/classifications/current/?site=2&type=10&tournament=0152")
dj = json.loads(datos.text)

print(__name__)

for i in dj['data'][0]['rank']:
    r = requests.get(i['imageUrlSizes']['S'])
    response.append([r.content, r])

for j in response:
    if j[1].ok:
        print(j[0])
        img_data = j[0]
        imagen = Image.open(BytesIO(img_data))
        imagen = imagen.resize((50,50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imagen)
        panel = tk.Label(root, image=img)
        elementos.append(panel)
        
for k in elementos:
    k.pack(side="bottom", fill="both", expand="yes")

root.mainloop()

'''
for i in dj['data'][0]['rank']:
    response = requests.get(i['imageUrlSizes']['L'])
    img_data = response.content
    imagen = Image.open(BytesIO(img_data))
    imagen = imagen.resize((300,205), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(imagen)
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    '''