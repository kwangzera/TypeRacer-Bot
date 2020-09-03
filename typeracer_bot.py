import time
from contextlib import suppress
from collections import namedtuple

from bs4 import BeautifulSoup
from pynput.keyboard import Controller

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# dict[name: lambda -> WebDriver]
DRIVER_FUNCS = dict(
    chrome=lambda: Chrome(executable_path="driver/chromedriver"),
    firefox=lambda: Firefox(executable_path="driver/geckodriver"),
)

def find_text(driver):
    """Return typeracer text."""
    # Get the HTML of the current page
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    span = soup.findAll("span")

    text = ""
    for i in span:
        if "unselectable" in str(i):
            text += i.text
    return text

def press_text(keyboard, text, delay):
    """Type `text` using `keyboard` to simulate real keypresses."""
    for i in text:
        time.sleep(delay)
        keyboard.press(i)
        keyboard.release(i)

def send_text(driver, text, delay):
    """Send `text` to text input box first working driver in `drivers` dict."""
    # Click the inputbox when it can be clicked
    elem = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
    for i in text:
        time.sleep(delay)
        elem.send_keys(i)

DriverInfo = namedtuple("DriverInfo", "name driver")
def get_driver(preferred=None, drivers=DRIVER_FUNCS):
    """Return first working driver name and instance in `drivers` dict."""
    if preferred in drivers:  # Hopefully None isn't a key in drivers
        with suppress(WebDriverException):
            return DriverInfo(preferred, drivers[preferred]())
    for name, func in drivers.items():
        with suppress(WebDriverException):
            return DriverInfo(name, func())
    raise LookupError(f"Driver not found: {preferred=!r}")

def main(link="https://play.typeracer.com", default=0.1, driver=None):
    if not isinstance(driver, WebDriver):
        driver = get_driver(preferred=driver).driver
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
        press_text(keyboard, text, delay)


if __name__ == "__main__":
    main()
