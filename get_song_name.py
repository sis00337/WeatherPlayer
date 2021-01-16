from get_top_artists import get_top_artists
import requests
import json


def get_song_name() -> None:
    """
    Get the name of songs by artist's name from the Itunes API.

    :return: None
    """
    artists = get_top_artists()
    SIZE = 5
    track_info = []
    song_dict_key = ['artistName', 'tracks']
    track_dict_key = ['trackName', 'genreName', 'previewUrl']
    for artist_name in artists:
        url = f'https://itunes.apple.com/search?term={artist_name}&entity=musicTrack&limit={SIZE}'
        song_list = []
        for number in range(SIZE):
            data = requests.get(url)
            response = data.json()
            try:
                track_dict_value = [response["results"][number]["trackName"],
                                    response["results"][number]["primaryGenreName"],
                                    response["results"][number]["previewUrl"]]
                track_dict = dict(zip(track_dict_key, track_dict_value))
                song_list.append(track_dict)
            except IndexError:
                pass
        song_dict_value = [artist_name.title().replace('+', ' '), song_list]
        song_dict = dict(zip(song_dict_key, song_dict_value))
        track_info.append(song_dict)

    write_json_file(track_info)


def write_json_file(track_info: list) -> None:
    """
    Write a new JSON file that includes the information of artists and the title of songs

    :return: None
    """
    filename = "artist_songs_dict_test.json"
    with open(filename, "w+") as file_object:
        json.dump(track_info, file_object)


def main():
    get_song_name()


if __name__ == '__main__':
    main()
