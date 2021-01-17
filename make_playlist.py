import json


def make_playlist(genre1: str, genre2: str, genre3: str):
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