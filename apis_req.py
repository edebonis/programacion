import requests

url = "https://andruxnet-world-cities-v1.p.rapidapi.com/"

querystring = {"query":"paris","searchby":"city"}

headers = {
	"X-RapidAPI-Key": "482ce9a392msh023c5dbb0d506efp108170jsn6a727fb71a15",
	"X-RapidAPI-Host": "andruxnet-world-cities-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)