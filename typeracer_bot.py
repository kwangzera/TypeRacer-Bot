'''
maybe try/except for error messages
drivers not just for chrome
features for practice mode and shared link
put everything into proper functions
2 more functions (separate text box selecting and typing
'''

import time
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
from selenium import webdriver

keyboard = Controller()

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://play.typeracer.com/")  # Open in new window


def bs4_find_text(driver):
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    txt = soup.findAll("span")
    print(3)

    words = []

    for i in txt:
        if "unselectable" in str(i):
            words.append(i.text)

    return "".join(words[:-1]) + f"{words[-1]}"


def bs4_type_text(para, delay):
    time.sleep(3)

    for i in para:
        time.sleep(delay)
        keyboard.press(i)
        keyboard.release(i)


def sel_find_text(driver):
    global elem

    # Input box
    # Rn is only selection
    elem = driver.find_element_by_xpath("//td/input[@type='text']")
    print("2")

    # Actual text
    sp = driver.find_elements_by_xpath("//span[@unselectable='on']")
    print("3")

    words = []

    for i in sp:
        words.append(i.text)

    return "".join(words[:-1]) + f" {words[-1]}"


def sel_type_text(para, delay):
    time.sleep(3)

    # For faster: .split(" ") for whole words
    # Will improve in future
    for i in para:
        time.sleep(delay)
        elem.send_keys(i)


def main():
    # Waits until input and then clicks "Enter a typing race"
    delay = float(input("Set your delay between keypresses: "))
    elem = driver.find_element_by_link_text("Enter a typing race").click()
    print(1)

    while True:
        input("Press enter when the race starts: ")
        para = bs4_find_text(driver)
        bs4_type_text(para, delay)


# The chrome window sometimes autocloses due to some pipe error
main()
