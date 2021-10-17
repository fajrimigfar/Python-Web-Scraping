import requests
import json

endpoint = "https://data.covid19.go.id/public/api/update.json"

def data_covid():
    response = requests.get(endpoint)
    data = json.loads(response.text)
    return data

update = data_covid().get("update")
print(update.get("penambahan"))
print(update.get("total"))
input("enter to exit")