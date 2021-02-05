import time
from contextlib import suppress

from bs4 import BeautifulSoup
from pynput.keyboard import Controller

from selenium.common.exceptions import TimeoutException, WebDriverException, UnexpectedAlertPresentException
from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def find_text(driver):
    """Returns typeracer text"""

    # Get the HTML of the current page
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    span = soup.findAll("span")

    # Text to be typed
    text = ""

    for i in span:
        if "unselectable" in str(i):
            text += i.text

    if text:
        print("- valid text successfully found")

    return text


def press_text(keyboard, text, delay):
    """Type `text` using `keyboard` to simulate real keypresses"""

    for i in text:
        time.sleep(delay)
        keyboard.press(i)
        keyboard.release(i)


def send_text(driver, text, delay):
    """Send `text` to text input box first working driver in `drivers` dict"""

    try:
        # Click the input box when it can be clicked
        wait = WebDriverWait(driver, 15)
        elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
    except TimeoutException:
        print("! input box not found within 15s")
    else:
        try:
            for i in text:
                time.sleep(delay)
                elem.send_keys(i)
        except UnexpectedAlertPresentException:
            pass

def get_driver(pref):
    """If pref in `drivers` dict, return respective driver"""

    # dict[name: lambda -> WebDriver]
    drivers = dict(
        chrome=lambda: Chrome(executable_path="drivers/chromedriver"),
        firefox=lambda: Firefox(executable_path="drivers/geckodriver"),
        edge=lambda: Edge(executable_path="drivers/msedgedriver"),
    )

    if pref in drivers:
        with suppress(WebDriverException):
            return drivers[pref]()

    raise LookupError(f"Driver and/or browser for driver '{pref}' does not exist")


def main(link="https://play.typeracer.com", default=0.1, driver="chrome"):
    driver = get_driver(driver)
    keyboard = Controller()

    # Open the link
    driver.get(link)

    # Able to run for multiple races
    while True:
        try:
            delay = float(input("Set your delay and press enter when the race starts: "))
        except ValueError:
            print(f"- default delay time set to {default}s")
            delay = default

        text = find_text(driver)
        time.sleep(1)
        send_text(driver, text, delay)


if __name__ == "__main__":
    main()
