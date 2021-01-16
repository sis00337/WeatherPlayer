from bs4 import BeautifulSoup
import requests


def TOP_URL() -> str:

    """
    Return the constant TOP_URL

    Location of top 200 artists from rolling stone.

    :return: a string of the url
    """

    return r"https://www.billboard.com/charts/artist-100"


def get_top_artists() -> list:

    """
    Submit get request to server and get top 100 artists.

    :return: a list of artists.
    """

    with requests.get(TOP_URL()) as top100:
        # Create BeautifulSoup object
        data = BeautifulSoup(top100.text, "html.parser")
        # get divs by class
        divs = data.findAll("div", {"class": "item-details__title"})
        # get the artist tags in the div
        artists = [div.text for div in divs]
        # reformat string for GET request
        artists_processed = [
            artist.lower().replace(" ", "+") for artist in artists
        ]
    return artists_processed


if __name__ == "__main__":
    get_top_artists()
