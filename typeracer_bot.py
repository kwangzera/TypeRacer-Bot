import time
from bs4 import BeautifulSoup
from pynput.keyboard import Controller
from selenium import webdriver


class TyperacerBot:
    def __init__(self, link="https://play.typeracer.com"):
        self.driver = webdriver.Chrome("driver/chromedriver.exe")
        self.keyboard = Controller()
        self.link = link
        self.text = ""

    def start(self):
        self.driver.get(self.link)

    def find_text(self):
        self.text = ""

        src = self.driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        txt = soup.findAll("span")

        for i in txt:
            if "unselectable" in str(i):
                self.text += i.text

        print(f"\"{self.text}\"")

    # Typing the text by simulating keypresses
    # After setting delay when race starts, immediately click the inputbox
    # Otherwise, the text will be typed wherever the caret is active
    def bs4_type_text(self, delay):
        for i in self.text:
            time.sleep(delay)
            self.keyboard.press(i)
            self.keyboard.release(i)

    # Typing the text by sending keys to an element
    # Letters of the text will be sent to the inputbox element
    # This method does not require manually clicking the inputbox but it's more laggy than the latter.
    def sel_type_text(self, delay):
        elem = self.driver.find_element_by_xpath("//td/input[@type='text']")

        for i in self.text:
            time.sleep(delay)
            elem.send_keys(i)


def main():
    # Pass your invite link below. Otherwise will default to https://play.typeracer.com
    bot = TyperacerBot()
    bot.start()

    while True:
        try:
            delay = float(input("Set your delay and press enter when the race starts: "))
        except ValueError:
            print("Delay set to default (0.1 seconds).")
            delay = 0.1

        bot.find_text()
        time.sleep(1)
        bot.bs4_type_text(delay)


main()
