# 🎵 Spotify Artist Scraper with Selenium

This Python project uses **Selenium WebDriver** to automate interaction with the public Spotify website interface.

The script performs the following tasks without requiring login:

1. Opens the [Spotify Search](https://open.spotify.com/search) page  
2. Accepts cookie consent if prompted  
3. Searches for an artist (e.g., *Michael Jackson*)  
4. Clicks on the artist’s public profile  
5. Scrolls through the artist's page  
6. Extracts the top 5 track titles  
7. Saves a screenshot of the artist's page  

---

## 📸 Example Output

```
Opened Spotify search page.
Accepted cookies.
Searched for Michael Jackson.
Clicked on Michael Jackson's artist page.
Scrolled to bottom of artist page.
Top tracks:
1. Billie Jean
2. Beat It
3. Thriller
4. Smooth Criminal
5. Black or White
Screenshot saved: saved_artist_pages/michael_jackson_artist_page.png
```

---

## 📂 Folder Structure

```
.
├── selenium_tests.py             # Main script
├── saved_artist_pages/           # Screenshots of artist pages
│   └── michael_jackson_artist_page.png
├── README.md                     # Project documentation
```

> 🔒 No Spotify login required. All actions are performed on publicly accessible content.

---

## 🛠️ Requirements

- Python 3.7+
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version

Install dependencies:

```bash
pip install selenium
```

---

## ▶️ Running the Script

1. Clone the repository or copy the script
2. Make sure `saved_artist_pages/` folder exists (or it will fail to save screenshot)
3. Run the script:

```bash
python selenium_tests.py
```

A Chrome window will open, navigate to Spotify, search for the artist, scroll the page, extract track names, and save a screenshot.

---

## ✅ Features

- Real browser interaction with Chrome via Selenium
- Handles cookie consent popup
- Works without needing Spotify login
- Easily customizable to search for other artists

---

## 🚀 To Do

- Add support for album or playlist scraping
- Add CSV export for extracted track names
- Add CLI argument for artist name

---

## 📄 License

This project is licensed under the MIT License.