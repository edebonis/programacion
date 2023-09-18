import requests
import json

resp = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

datosDict = json.loads(resp.text)

weight = datosDict['weight']
name = datosDict['abilities'][0]['ability']['name']
print(name)
