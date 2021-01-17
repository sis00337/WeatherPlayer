import json


def open_json_file() -> dict:
    """
    Open the JSON file that includes the information of artists and the title of songs.

    :return: a JSON object
    """
    filename = 'artist_songs_dict_test.json'
    with open(filename) as file_object:
        json_obj = json.load(file_object)
    return json_obj


def get_genre():
    genre_set = set()
    json_obj = open_json_file()
    for index in range(len(json_obj)):
        tracks = json_obj[index]['tracks']
        for element in tracks:
            genre_set.add(element['genreName'])
    print(genre_set)


def main():
    get_genre()


if __name__ == '__main__':
    main()

