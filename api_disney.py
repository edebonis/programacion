import requests
import json

url = "https://api.disneyapi.dev/characters"

# Create an object of tkinter ImageTk
while url:
    datos = requests.get(url)
    print(datos.text)
    dj = json.loads(datos.text)
    for i in dj['data']:
        if i.get('name'):
            print(i['name'])
        if i.get('imageUrl'):
            print(i['imageUrl'])
            
    url = dj.get('nextPage')


# Create a Label Widget to display the text or Image

label.pack()

win.mainloop()