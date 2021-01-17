import json

with open('artist_songs_dict_test.json') as json_file:
    data = json.load(json_file)
    genrelist = []
    for artist in data:
        track = artist["tracks"]
        for song in track:
            genrelist.append(song["genreName"])
    genreset = set(genrelist)
    print(genreset)
