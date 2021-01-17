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
                    if song["genreName"] == genre1:
                        song_data = {"artistName": artist["artistName"]}
                        song_data["trackViewUrl"] = song["trackViewUrl"]
                        song_data["previewUrl"] = song["previewUrl"]
                        song_data["thumbnail"] = song["thumbnail"]
                        playlist.append(song_data)
    return playlist