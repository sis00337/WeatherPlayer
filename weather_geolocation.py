import requests
import json


def get_weather_info(search_keyword):
    json_obj = geolocation_api_call(search_keyword)
    location_dict = get_coordinates(json_obj)
    latitude = location_dict['lat']
    longitude = location_dict['lng']
    weather_json = weather_api_call(latitude, longitude)
    return weather_json


def geolocation_api_call(search_keyword):
    """The API url format is https://geocode.search.hereapi.com/v1/geocode?apikey=YOUR_API_KEY&q=ADDRESS_TO_SEARCH

    :postcondition: Submit GET request to API url and process the response into usable JSON data
    :return: JSON data
    """

    # Assemble API call components
    api_key = "apikey=" + "qyMNiLbm-lx7gegxL4ixX_w5kYqAQJTO1BhgbmDOtt4"
    # REPLACE WITH USER INPUT FROM HTML
    search_address = f"&q={search_keyword}"
    base_url = "https://geocode.search.hereapi.com/v1/geocode?"

    # Send GET request, load response into JSON format
    response = requests.get(base_url + api_key + search_address)
    response.raise_for_status()
    json_data = json.loads(response.text)

    return json_data


def get_coordinates(json_data):
    """
    :param json_data:
    :return: longitude and latitude as a dictionary
    """

    return json_data['items'][0]['position']


def weather_api_call(latitude: str, longitude: str):
    """API url format is https://api.openweathermap.org/data/2.5/weather?lat=LATITUDE&lon=LONGITUDE&appid=API_KEY&units=metric

        :param: latitude and longitude must be numbers as strings
        :return: JSON data for weather
    """

    # Assemble API call components
    api_key = "fb948a68fea5555ccf35cc9260208dd9"
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    url_lat = f'lat={latitude}'
    url_long = f'&lon={longitude}'
    url_api_key = f'&appid={api_key}'

    # Send GET request, load response into JSON format
    response = requests.get(base_url + url_lat + url_long + url_api_key + "&units=metric")
    response.raise_for_status()
    json_data = json.loads(response.text)

    return json_data


def get_temperature(json_data):
    return json_data['main']['temp']


def get_city_name(json_data):
    return json_data['name']


def sunny_or_cloudy(json_data):
    return json_data['weather'][0]['main']


def main():
    """Test that the functions are working properly"""
    json_geolocation = geolocation_api_call('New York')
    lat_long = get_coordinates(json_geolocation)
    latitude = lat_long['lat']
    longitude = lat_long['lng']
    print(f'{lat_long}\n'
          f'Latitude: {latitude}\n'
          f'Longitude: {longitude}\n')

    json_weather = weather_api_call(latitude, longitude)

    print(f'Temperature: {get_temperature(json_weather)} degrees Celsius')
    print(f'City: {get_city_name(json_weather)}')
    print(f'Sky Condition: {sunny_or_cloudy(json_weather)}')


if __name__ == '__main__':
    main()
