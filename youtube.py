import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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

def open_youtube():
    global driver, body
    if driver is None:
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com")
        time.sleep(1)
        body = driver.find_element(By.TAG_NAME, "body")
        return "Opening YouTube sir"
    else:
        return "YouTube already open hai sir"

def search_youtube(query):
    global driver, body
    if driver is not None:
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        body = driver.find_element(By.TAG_NAME, "body")
        return f"Searching {query} on YouTube"
    else:
        return "YouTube abhi open nahi hai sir"

def play_nth_video(n):
    global driver, body
    if driver is not None:
        videos = driver.find_elements(By.ID, "video-title")
        if len(videos) >= n:
            videos[n - 1].click()
            time.sleep(3)
            body = driver.find_element(By.TAG_NAME, "body")
            return f"Playing video number {n}"
        else:
            return f"Sir, sirf {len(videos)} videos available hain"
    else:
        return "YouTube abhi open nahi hai sir"

def control_video(command):
    global body, driver
    if driver is None or body is None:
        return "YouTube abhi open nahi hai sir"

    if command == "play" or command == "pause":
        body.send_keys("k")
        return f"{command}ing video sir"
    elif command == "mute":
        body.send_keys("m")
        return "Muted video sir"
    elif command == "unmute":
        body.send_keys("m")
        return "Unmuted video sir"
    elif command == "fullscreen":
        body.send_keys("f")
        return "Fullscreen video sir"
    elif command in ["minimise", "exit fullscreen"]:
        body.send_keys(Keys.ESCAPE)
        return "Exited fullscreen"
    elif command == "forward":
        body.send_keys("l")
        return "Forward 10 sec"
    elif command in ["back", "rewind"]:
        body.send_keys("j")
        return "Rewind 10 sec"
    elif command == "volume up":
        body.send_keys(Keys.ARROW_UP)
        return "Volume up sir"
    elif command == "volume down":
        body.send_keys(Keys.ARROW_DOWN)
        return "Volume down sir"
    elif command == "next video":
        body.send_keys(Keys.SHIFT, "n")
        return "Next video sir"
    elif command == "previous video":
        body.send_keys(Keys.SHIFT, "p")
        return "Previous video sir"
    else:
        return "Unknown command"

def close_youtube():
    global driver, body
    if driver is not None:
        driver.quit()
        driver = None
        body = None
        return "Closing YouTube sir"
    else:
        return "YouTube already closed"