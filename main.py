import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic


def check_authentication():
    """Check if browser.json exists, otherwise show instructions and exit."""
    if not os.path.exists("browser.json"):
        print("browser.json not found.")
        print("You need to authenticate with YouTube Music first.")
        print("Run one of these commands in your terminal from this project folder:\n")
        print("  Mac:     pbpaste | ytmusicapi browser")
        print("  Windows: ytmusicapi browser\n")
        print("Copy the request headers from Firefox first.")
        print("This will create browser.json.")
        exit()


def scrape_songs(date):
    """Scrape the top 100 song titles for a given date from Bakeboard."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
    url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")]
    print(f"Found {len(song_names)} songs.")
    return song_names


def get_or_create_playlist(yt, playlist_name, date):
    """Return the existing playlist's id, or create a new one if it doesn't exist."""
    playlists = yt.get_library_playlists(limit=100)

    for p in playlists:
        if p["title"] == playlist_name:
            print("This playlist already exists.")
            return p["playlistId"], False 

    playlist_id = yt.create_playlist(
        playlist_name,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")
    return playlist_id, True 


def add_songs_to_playlist(yt, playlist_id, song_names):
    """Search each song and add the top result to the playlist."""
    for song in song_names:
        try:
            search_results = yt.search(song, filter="songs", limit=1)
            yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
            print(f"Added: {song}")
        except Exception as e:
            print(f"Skipped: {song} | Reason: {e}")

def main():
    check_authentication()

    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

    song_names = scrape_songs(date)

    yt = YTMusic("browser.json")
    playlist_name = f"{date} Billboard 100"
    playlist_id, is_new = get_or_create_playlist(yt, playlist_name, date)

    if is_new:
        add_songs_to_playlist(yt, playlist_id, song_names)


if __name__ == "__main__":
    main()