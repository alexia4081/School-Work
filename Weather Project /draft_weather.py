#Alexia Diaz
# 9.3 Assignment
import json
import weather_service

# Create a Python Application which asks the user for their zip code or city.
zip_code = input("Enter zip code: ")
city_name = input("Enter City Name: ")

if zip_code != '':
    weather_json = weather_service.get_weather_by_zip(zip_code)
    print(json.dumps(weather_json, indent=4, sort_keys=True))
elif city_name != '':
    weather_json = weather_service.get_weather_by_city(city_name)
    print(json.dumps(weather_json, indent=4, sort_keys=True))
