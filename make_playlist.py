import json


def make_playlist(genre1: str, genre2: str, genre3: str):
    """

    :param: string or 0
    :return: list of dictionaries
    """
    with open('artist_songs_dict_test.json') as json_file:
        data = json.load(json_file)
        playlist = []
        genres = [genre1, genre2, genre3]
        for artist in data:
            track = artist["tracks"]
            for song in track:
                for genre in genres:
                    if song["genreName"] == genre:
                        song_data = {"artistName": artist["artistName"], "trackViewUrl": song["trackViewUrl"],
                                     "previewUrl": song["previewUrl"], "thumbnail": song["thumbnail"]}
                        playlist.append(song_data)
    return playlist



def weather_to_song_convertor(weather_condition: str) -> list:
    """Return list of songs depending on weather conditions"""

    POSSIBLE_WEATHER = {'Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Mist', 'Smoke', 'Haze', ' Dust',
                        ' Fog', ' Sand', ' Dust', ' Ash', ' Squall', ' Tornado', ' Clear', ' Clouds'}

    if weather_condition == 'Thunderstorm':
        songs = make_playlist('Hard Rock', 'Metal', 'Rock')
    elif weather_condition == 'Drizzle' or weather_condition == 'Rain':
        songs = make_playlist('Alternative', 'Soul', 'Rap')
    elif weather_condition == 'Snow':
        songs = make_playlist('Christmas', 'Musicals', 0)
    elif weather_condition == 'Clear':
        songs = make_playlist('Disco', 'Country', 'Pop')
    elif weather_condition == 'Clouds':
        songs = make_playlist('Soundtrack', 0, 0)
    else:
        songs = make_playlist('Dance', "K-Pop", 'Pop Latino')

    return songs


def main():
    """Test the function"""
    songs = make_playlist('Dance', "K-Pop", 'Pop Latino')
    print(songs)
    more_songs = weather_to_song_convertor('Fog')
    print(more_songs)


if __name__ == '__main__':
    main()