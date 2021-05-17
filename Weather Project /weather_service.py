import requests

api_key = 'c8c72ade501e8dc2ae754aced82bb3ad'
zip_api_uri = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}'
city_name_api_uri = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# Get weather by zip
def get_weather_by_zip(zipcode):
    uri = zip_api_uri.format(zipcode, api_key)
    return requests.get(uri).json()


# Get weather by city
def get_weather_by_city(city):
    uri = city_name_api_uri.format(city, api_key)
    return requests.get(uri).json()
