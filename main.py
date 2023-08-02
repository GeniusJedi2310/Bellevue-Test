import json, requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "5e11ab250139dff4250bf6bb5346fb60"
city_or_zip = input("Please enter a city or ZIP code here:")

url = f"{base_url}?q={city_or_zip}&units=imperial&APPID={appid}"
print(url)
print ()

response = requests.get(url)
unformated_data = response.json()

#print(unformatted_data)

temp_min = unformated_data["main"]["temp_min"]
print(f"The lowest temperature is {temp_min}")

temp = unformated_data["main"]["temp"]
print(f"The current temperature is {temp}")

temp_max = unformated_data["main"]["temp_max"]
print(f"The highest temperature is {temp_max}")