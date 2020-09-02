import time
from bs4 import BeautifulSoup
from pynput.keyboard import Controller

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_text(driver):
    # Resetting text
    text = ""

    # Get the HTML of the current page
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    span = soup.findAll("span")

    for i in span:
        if "unselectable" in str(i):
            text += i.text

    if text:
        print("- valid text successfully found")

    return text

def keypress_type(keyboard, text, delay):
    for i in text:
        time.sleep(delay)
        keyboard.press(i)
        keyboard.release(i)

def keysend_type(driver, text, delay):
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


def main(link="https://play.typeracer.com", delay=0.1):
    driver = webdriver.Chrome("driver/chromedriver.exe")
    keyboard = Controller()
    # Open the link
    driver.get(link)

    # Able to run for multiple races
    while True:
        try:
            delay = float(input("Set your delay and press enter when the race starts: "))
        except ValueError:
            print(f"- using previous delay time of {delay}s")

        text = find_text(driver)
        time.sleep(1)
        keypress_type(keyboard, text, delay)


main()
