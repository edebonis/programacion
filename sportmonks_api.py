import requests

url = "https://api.unidadeditorial.es/sports/v1/classifications/current/?site=2&type=10&tournament=0152"

response = requests.get(url)

print(response.text)