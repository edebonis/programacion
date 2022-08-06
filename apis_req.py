import requests
import json
import hashlib
import pprint

pp = pprint.PrettyPrinter(depth=7)

private = "042b70f68353cb5f3f4b3c475a3ba24db0ab03db"
public = "6ad17068fa597efb20f9265544418b46"
ts = 12
hashe = hashlib.md5((str(ts) + private + public).encode())
print(hashe.hexdigest())
url = "https://gateway.marvel.com/v1/public/comics?ts={}&apikey={}&hash={}"
url2 = "http://gateway.marvel.com/v1/public/comics/376/characters?ts={}&apikey={}&hash={}"
response = requests.get(url.format(ts, public, hashe.hexdigest()))
responessw = requests.get('https://swapi.dev/api/films/')
datosw = json.loads(responessw.text)
datos = json.loads(response.text)
#pp.pprint(datosw)
for i in datosw['results']:
    print(i['title'])