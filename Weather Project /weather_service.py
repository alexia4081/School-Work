import requests

api_key = 'c8c72ade501e8dc2ae754aced82bb3ad'
zip_api_uri = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}'
city_name_api_uri = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
timeout_exception = 'A timeout has occurred while fetching data'
connection_exception = 'A error has occurred while attempting to make a connection to web service'


# Get weather by zip
def get_weather_by_zip(zipcode):
    try:
        uri = zip_api_uri.format(zipcode, api_key)
        result = requests.get(uri).json()

    except requests.exceptions.Timeout:
        result = timeout_exception
    except requests.exceptions.ConnectionError:
        result = connection_exception

    return result


# Get weather by city
def get_weather_by_city(city):
    try:
        uri = city_name_api_uri.format(city, api_key)
        result = requests.get(uri).json()
    except requests.exceptions.Timeout:
        result = timeout_exception
    except requests.exceptions.ConnectionError:
        result = connection_exception

    return result
