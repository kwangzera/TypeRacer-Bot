import time
from bs4 import BeautifulSoup
from pynput.keyboard import Controller

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TyperacerBot:
    def __init__(self, link):
        self.driver = webdriver.Chrome("driver/chromedriver.exe")
        self.keyboard = Controller()
        self.link = link
        self.text = ""

    def start(self):
        # Open the link
        self.driver.get(self.link)

    def find_text(self):
        # Resetting text
        self.text = ""

        # Get the HTML of the current page
        src = self.driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        span = soup.findAll("span")

        for i in span:
            if "unselectable" in str(i):
                self.text += i.text

        if self.text:
            print("- valid text successfully found")

    def keypress_type(self, delay):
        for i in self.text:
            time.sleep(delay)
            self.keyboard.press(i)
            self.keyboard.release(i)

    def keysend_type(self, delay):
        try:
            # Click the inputbox when it can be clicked
            wait = WebDriverWait(self.driver, 15)
            elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
        except TimeoutException:
            print("! inputbox not found within 15s")
        else:
            for i in self.text:
                time.sleep(delay)
                elem.send_keys(i)


def main():
    # Default link and delay time
    link = "https://play.typeracer.com"
    delay = 0.1

    bot = TyperacerBot(link)
    bot.start()

    # Able to run for multiple races
    while True:
        try:
            delay = float(input("Set your delay and press enter when the race starts: "))
        except ValueError:
            print("- default delay time set to 0.1s")

        bot.find_text()
        time.sleep(1)
        bot.keypress_type(delay)


main()
