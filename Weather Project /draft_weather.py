#Alexia Diaz
# 9.3 Assignment
import json
import weather_service

# Create a Python Application which asks the user for their zip code or city.
while True:
    zip_code = input("Enter zip code: ")
    city_name = input("Enter City Name: ")

    if zip_code != '' and zip_code.isnumeric():
        weather_json = weather_service.get_weather_by_zip(zip_code)
        print(json.dumps(weather_json, indent=4, sort_keys=True))
    elif city_name != '' and city_name.isalpha():
        weather_json = weather_service.get_weather_by_city(city_name)
        print(json.dumps(weather_json, indent=4, sort_keys=True))
    else:
        print("The data you supplied is invalid")
        continue

    exit_app = input("\nWould you like to exit application (Yes or No): ").upper()
    if exit_app == 'YES':
        break
