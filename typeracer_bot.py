import time
from bs4 import BeautifulSoup
from pynput.keyboard import Controller
from selenium import webdriver
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

        # Get the html of the current page
        src = self.driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        txt = soup.findAll("span")

        for i in txt:
            if "unselectable" in str(i):
                self.text += i.text

        print(f"\"{self.text}\"")

    def bs4_type_text(self, delay):
        for i in self.text:
            time.sleep(delay)
            self.keyboard.press(i)
            self.keyboard.release(i)

    def sel_type_text(self, delay):
        # Click the input bot when it can be clicked
        wait = WebDriverWait(self.driver, 15)
        elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))

        for i in self.text:
            time.sleep(delay)
            elem.send_keys(i)


def main():
    bot = TyperacerBot("https://play.typeracer.com")
    bot.start()

    # Able to run for multiple races
    while True:
        try:
            delay = float(input("Set your delay and press enter when the race starts: "))
        except ValueError:
            print("Delay set to default (0.1 seconds).")
            delay = 0.1

        bot.find_text()
        time.sleep(1)
        bot.sel_type_text(delay)


main()
