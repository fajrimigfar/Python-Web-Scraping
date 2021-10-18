# Program Web Scraping

import requests
import json

endpoint = "https://data.covid19.go.id/public/api/update.json"

def data_covid():
    response = requests.get(endpoint)
    data = json.loads(response.text)
    return data

update = data_covid().get("update")
penambahan = update.get("penambahan")
total = update.get("total")

tanggal = penambahan.get("tanggal")
print(tanggal)
penambahan_positif = penambahan.get("jumlah_positif")
print(penambahan_positif)
penambahan_meninggal = penambahan.get("jumlah_meninggal")
print(penambahan_meninggal)
penambahan_sembuh = penambahan.get("jumlah_sembuh")
print(penambahan_sembuh)
total_positif = total.get("jumlah_positif")
print(total_positif)
total_meninggal = total.get("jumlah_meninggal")
print(total_meninggal)
total_sembuh = total.get("jumlah_sembuh")
print(total_sembuh)
input("enter to exit")
