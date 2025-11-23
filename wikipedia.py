# wikipedia.py
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None

number_map = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "sixth": 6,
    "seventh": 7,
    "eighth": 8,
    "ninth": 9,
    "tenth": 10
}

def open_wiki():
    """
    Open Wikipedia (English main page). Returns a Hindi status string.
    """
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.get("https://en.wikipedia.org")
        time.sleep(2)
        return "Wikipedia khol di hai sir"
    else:
        return "Wikipedia pehle se khuli hui hai sir"

def search_wiki(query):
    """
    Search Wikipedia for `query`. Uses Special:Search to ensure search-results page.
    """
    global driver
    if driver is None:
        return "Wikipedia abhi open nahi hai sir — pehle open_wiki() chalao"
    try:
        q = urllib.parse.quote(query)
        # Directly navigate to search results (reliable across setups)
        driver.get(f"https://en.wikipedia.org/w/index.php?search={q}&ns0=1")
        time.sleep(2)
        return f"Wikipedia par '{query}' search kar diya"
    except Exception as e:
        return f"Search mei error aaya: {e}"

def open_nth_result(n):
    """
    From the search-results page, open the nth result.
    n can be integer (1-based) or string like "first".
    """
    global driver
    if driver is None:
        return "Wikipedia abhi open nahi hai sir — pehle open_wiki() chalao"
    try:
        # accept string names too
        if isinstance(n, str):
            n_lower = n.lower()
            n = number_map.get(n_lower, None)
            if n is None:
                try:
                    n = int(n_lower)
                except:
                    return "Number samajh nahi aaya sir"
        # First check if current page is already an article (no results list)
        # If so, just return that we're already on an article.
        # Otherwise find result links from search page.
        time.sleep(1)
        # Common selector for search-result headings
        result_links = driver.find_elements(By.CSS_SELECTOR, "div.mw-search-result-heading > a")
        if len(result_links) == 0:
            # Sometimes search redirects directly to an article; try checking first heading
            headings = driver.find_elements(By.ID, "firstHeading")
            if headings:
                return "Yeh page pehle se article hai — same page khul gaya"
            else:
                return "Koi search results nahi mili"
        if len(result_links) >= n and n >= 1:
            result_links[n-1].click()
            time.sleep(2)
            return f"Search result number {n} khol diya"
        else:
            return f"Sir, sirf {len(result_links)} results available hain"
    except Exception as e:
        return f"open_nth_result mei error: {e}"

def close_wiki():
    global driver
    if driver is not None:
        driver.quit()
        driver = None
        return "Wikipedia is closing"
    else:
        return "Wikipedia already closed"
