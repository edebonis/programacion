import requests
import json
import pprint

#pp = pprint.PrettyPrinter(depth=8)
for i in range(1,10):
    datos = requests.get("https://script.google.com/macros/s/AKfycbwIQi_DScVfwbNndXE3i_DKC_AiSIx07_6xPzgJlWvDkLrH_ETRIG3Td5We2h3ooIaDzw/exec?m={}".format(i))
    dj = json.loads(datos.text)
    print(dj['docente'],dj['nombre'])
#print(type(dj['data'][0]['rank']))
#pp.pprint(dj['data'][0]['rank'])
#pp.pprint(dj)

