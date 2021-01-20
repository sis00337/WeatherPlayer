import os

import googleapiclient.discovery


def search_youtube(artist_name: str, track_name: str):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCk8JlIji8Zj8ZHKMDI3IsZP89H-sOjRyM"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=2,
        q=artist_name + track_name
    )
    response = request.execute()

    return response


def find_data(search_results: dict):
    video_id = search_results["items"][0]["id"]["videoId"]
    video_title = search_results["items"][0]["snippet"]["title"]
    thumbnail = search_results["items"][0]["snippet"]["thumbnails"]["medium"]["url"]

    video_data = {"videoId": video_id, "videoTitle": video_title, "thumbnail": thumbnail}
    print(f"https://www.youtube.com/watch?v=" + video_id)
    return video_data


def main():
    artist = "Taylor Swift"
    song_title = "Blank Space"
    search_results = search_youtube(artist, song_title)
    print(search_results)
    video_data = find_data(search_results)
    print(video_data)


if __name__ == "__main__":
    main()