from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    # 1. Open Spotify search page
    driver.get("https://open.spotify.com/search")
    print("Opened Spotify search page.")
    time.sleep(5)

    # 2. Accept cookies if the button is present
    try:
        cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]")))
        cookie_button.click()
        print("Accepted cookies.")
    except:
        print("No cookie consent button found or already accepted.")
    
    time.sleep(5)

    # 3. Search for an artist
    search_artist = 'Michael Jackson'
    search_input = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    search_input.send_keys(search_artist)
    search_input.send_keys(Keys.RETURN)
    print(f"Searched for {search_artist}.")
    time.sleep(5)

    # 4. Scroll down a bit to load the artist section
    driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(3)

    # 5. Click on the first artist card by partial match of href or text
    artist_card = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/artist/') and .//span[text()='{search_artist}']]")))
    artist_card.click()
    print(f"Clicked on {search_artist}'s artist page.")
    time.sleep(5)

    # 6. Scroll down on artist page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scrolled to bottom of artist page.")
    time.sleep(3)

    # 7. Extract top track names
    print("Top tracks:")
    track_titles = driver.find_elements(By.XPATH, "//div[@data-testid='tracklist-row']//div[@dir='auto'][1]")
    for i, track in enumerate(track_titles[:5], start=1):
        print(f"{i}. {track.text}")

    # 8. Take a screenshot
    screenshot_path = f"saved_artist_pages/{search_artist}_artist_page.png".replace(" ", "_").lower()
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

finally:
    driver.quit()
