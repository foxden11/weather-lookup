import requests

city = input("City: ")

try:
    geo = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=" + city + "&count=1")
    geodata = geo.json()

    if "results" in geodata:
        lat = geodata["results"][0]["latitude"]
        lon = geodata["results"][0]["longitude"]
        weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) +  
        "&current=temperature_2m")
        data = weather.json()
        print(city, data["current"]["temperature_2m"], "°C")
    else:
        print("City not found")

except requests.exceptions.RequestException as e:
        print("Network problem:", e)