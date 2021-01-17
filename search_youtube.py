import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

artist_name = "Taylor Swift"
track_name = "Blank Space"
search_query = artist_name + track_name

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_desktop.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=2,
        q=search_query,
        type="video"
    )
    response = request.execute()

    search_results = response["items"]
    first_result = search_results[0]
    id_info = first_result["id"]
    video_id = id_info["videoId"]
    print(f"https://www.youtube.com/embed/" + video_id)


if __name__ == "__main__":
    main()