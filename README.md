# 🎵 Muzical Time Machine

Travel back in time and relive the top songs from any date in history! This project scrapes the Billboard Hot 100 chart for a given date and automatically creates a matching playlist on YouTube Music.

## How It Works

1. You enter a date (e.g. `2026-04-18`)
2. The script scrapes the top 100 song titles for that date from [Bakeboard Hot 100](https://appbrewery.github.io/bakeboard-hot-100/) (a Billboard Hot 100 clone)
3. It searches for each song on YouTube Music
4. It creates a new private playlist and adds all the songs it could find

## Requirements

- Python 3.8+
- A Google account (any account works with YouTube Music)
- [Firefox](https://www.firefox.com/en-GB/) browser (needed once, for authentication)

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd Muzical_Time_Machine
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install requests beautifulsoup4 ytmusicapi
   ```

## Authentication Setup (One-Time)

`ytmusicapi` needs to borrow your browser's YouTube Music login session. This only needs to be done once (cookies may expire over time — if authentication stops working, just repeat these steps).

1. Open **Firefox** and go to [music.youtube.com](https://music.youtube.com). Make sure you're logged in.
2. Open Developer Tools:
   - Mac: `Cmd + Option + I`
   - Windows/Linux: `Ctrl + Shift + I`
3. Click the **Network** tab, and filter requests by typing `browse`.
4. Refresh the page (or click Home / Library) until you see a `browse?...` request to `music.youtube.com`.
5. Right-click it → **Copy** → **Copy Request Headers**.
6. In your terminal, from the project folder, run:

   **Mac:**
   ```bash
   pbpaste | ytmusicapi browser
   ```

   **Windows / Linux:**
   ```bash
   ytmusicapi browser
   ```
   Paste the headers when prompted, then press `Ctrl+D` (or `Ctrl+Z` on Windows) followed by Enter.

This creates a `browser.json` file in your project folder — **do not commit this file**, it contains your login session.

## Usage

Run the script:
```bash
python main.py
```

You'll be prompted to enter a date:
```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2026-04-18
```

The script will:
- Scrape the top 100 songs for that date
- Create a playlist named `2026-04-18 Billboard 100` on your YouTube Music account (skips creation if it already exists)
- Search for and add each song, skipping any that can't be found

Once it's done, open **YouTube Music** → **Library** to see your new playlist! 🎉

## Project Structure

```
Muzical_Time_Machine/
├── main.py              # Main script
├── browser.json         # Auth session (auto-generated, not committed)
├── .gitignore
└── README.md
```

## Notes

- Some songs may not be found on YouTube Music or may fail to add — these are skipped automatically, and the console will show which ones.
- Bakeboard doesn't have every possible date — check the calendar widget on the [Bakeboard site](https://appbrewery.github.io/bakeboard-hot-100/) for available dates.
- To use the real Billboard Hot 100 site instead of Bakeboard, update the URL in `scrape_songs()` — just be aware Billboard may change its page structure or introduce anti-scraping measures over time.

## Credits

Built as part of [The App Brewery](https://www.appbrewery.com/)'s Python course.
