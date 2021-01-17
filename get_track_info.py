from get_top_artists import get_top_artists
import requests
import json


def SEARCH_HOW_MANY_SONGS():
    return 5


def dictionary_maker() -> None:
    """
    Store the information of tracks to a list of dictionaries.

    :return: None
    """
    artists = get_top_artists()
    track_info = []
    song_dict_key = ['artistName', 'tracks']
    track_dict_key = ['trackName', 'genreName', 'previewUrl', 'thumbnail']
    for artist_name in artists:
        song_list = get_track_info(artist_name, track_dict_key)
        song_dict_value = [artist_name.title().replace('+', ' '), song_list]
        song_dict = dict(zip(song_dict_key, song_dict_value))
        track_info.append(song_dict)

    write_json_file(track_info)


def get_track_info(artist_name: str, track_dict_key: list) -> list:
    """
    Get thr information of tracks from iTunes API.
    """
    url = f'https://itunes.apple.com/search?term={artist_name}&entity=musicTrack&limit={SEARCH_HOW_MANY_SONGS()}'
    song_list = []
    for number in range(SEARCH_HOW_MANY_SONGS()):
        data = requests.get(url)
        response = data.json()
        try:
            track_dict_value = [response["results"][number]["trackName"],
                                response["results"][number]["primaryGenreName"],
                                response["results"][number]["previewUrl"],
                                response["results"][number]["artworkUrl100"]]
            track_dict = dict(zip(track_dict_key, track_dict_value))
            song_list.append(track_dict)
        except IndexError:
            pass
    return song_list


def write_json_file(track_info: list) -> None:
    """
    Write a new JSON file that includes the information of artists and the title of songs

    :return: None
    """
    filename = "artist_songs_dict_test.json"
    with open(filename, "w+") as file_object:
        json.dump(track_info, file_object)


def main():
    dictionary_maker()


if __name__ == '__main__':
    main()
