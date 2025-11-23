import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = None
body = None

number_map = {
    "first": 1,
    "second": 2,
    "third": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}

def open_chrome():
    global driver, body
    if driver is None:
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")  # ✅ open google instead of chrome.com
        time.sleep(3)
        body = driver.find_element(By.TAG_NAME, "body")
        return "Opening Chrome sir"
    else:
        return "Chrome already open hai sir"

def search_chrome(query):
    global driver, body
    if driver is not None:
        try:
            search_box = driver.find_element(By.NAME, "q")  # ✅ google search bar
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            body = driver.find_element(By.TAG_NAME, "body")
            return f"Searching {query} on Chrome"
        except Exception as e:
            return f"Search bar nahi mila sir: {str(e)}"
    else:
        return "Chrome abhi open nahi hai sir"

def play_nth_website(n):
    global driver, body
    if driver is not None:
        results = driver.find_elements(By.CSS_SELECTOR, "h3")  # ✅ google search results
        if len(results) >= n:
            results[n - 1].click()
            time.sleep(3)
            body = driver.find_element(By.TAG_NAME, "body")
            return f"Opening website number {n}"
        else:
            return f"Sir, sirf {len(results)} results available hain"
    else:
        return "Chrome abhi open nahi hai sir"

def close_chrome():
    global driver, body
    if driver is not None:
        driver.quit()
        driver = None
        body = None
        return "Closing Chrome sir"
    else:
        return "Chrome already closed"