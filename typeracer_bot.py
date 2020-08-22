import time
from bs4 import BeautifulSoup
from pynput.keyboard import Controller
from selenium import webdriver


class TyperacerBot:
    def __init__(self, link):
        self.driver = webdriver.Chrome("driver/chromedriver.exe")
        self.keyboard = Controller()
        self.link = link
        self.text = ""

    def start(self):
        self.driver.get(self.link)

    def find_text(self):
        src = self.driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        txt = soup.findAll("span")

        for i in txt:
            if "unselectable" in str(i):
                self.text += i.text

        print(f"\"{self.text}\"")

    def type_text(self, delay):
        for i in self.text:
            time.sleep(delay)
            self.keyboard.press(i)
            self.keyboard.release(i)

        self.text = ""


def main():
    custom = input("Custom link? Y/N: ")
    
    if custom.upper() == "Y":
        link = input("Custom link: ")
    else:
        link = "https://play.typeracer.com"

    bot = TyperacerBot(link)
    bot.start()

    while True:
        try:
            delay = float(input("Set your delay and press enter when the race starts: "))
        except ValueError:
            print("Invalid input. Delay set to 0.1 seconds.")
            delay = 0.1

        bot.find_text()
        time.sleep(1)
        bot.type_text(delay)


main()
