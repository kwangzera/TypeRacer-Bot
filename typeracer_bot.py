import time
from contextlib import suppress

from bs4 import BeautifulSoup
from pynput.keyboard import Controller

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# dict[name: WebDriver]
DRIVER_CLASSES = {
    "chrome": Chrome,
    "firefox": Firefox,
    "edge": Edge,
}


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

    if text:
        print("- valid text successfully found")

    return text


def press_text(keyboard, text, delay):
    """Type `text` using `keyboard` to simulate real keypresses."""

    for i in text:
        time.sleep(delay)
        keyboard.press(i)
        keyboard.release(i)


def send_text(driver, text, delay):
    """Send `text` to text input box first working driver in `drivers` dict."""

    try:
        # Click the inputbox when it can be clicked
        wait = WebDriverWait(driver, 15)
        elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
    except TimeoutException:
        print("! inputbox not found within 15s")
    else:
        for i in text:
            time.sleep(delay)
            elem.send_keys(i)


def get_driver(preferred=None, drivers=None):
    """Return first working driver instance in `drivers` dict."""

    if drivers is None:
        drivers = DRIVER_CLASSES

    if preferred in drivers:  # Hopefully None isn't a key in drivers
        with suppress(WebDriverException):
            return drivers[preferred](executable_path=f"drivers/{preferred}driver")

    for name, cls in drivers.items():
        with suppress(WebDriverException):
            return cls(executable_path=f"drivers/{name}driver")

    raise LookupError(f"Driver not found: {preferred=}")


def main(link="https://play.typeracer.com", default=0.1, driver=None):
    if not isinstance(driver, WebDriver):
        driver = get_driver(preferred=driver)

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
