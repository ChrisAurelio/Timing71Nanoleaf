from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nanoleafapi import Nanoleaf
from nanoleafapi import RED, YELLOW, GREEN, WHITE
import time

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
#options.add_argument("--headless")

nl = Nanoleaf()     # Enter Nanoleaf IP Address
nl.set_brightness(30)

def main():
    setup()
    timingLoop()

def setup():

    print("Enter Timing71 ID: ")
    timingID = input()
    url = "https://timing71.org/replay/" + timingID

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    global driver
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver.get(url)

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[1]/ul/li[1]/a/span')))
        driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/ul/li[1]/a/span').click()
    except TimeoutException:
        print("Timing71 failed to load")

def timingLoop():
    
    while (True):
        if (driver.find_elements_by_css_selector('#app > div > div > div > div.timing-screen-header > div.flag-status.flag-status-green')):
            nl.set_color(GREEN)
            time.sleep(10)
        elif (driver.find_elements_by_css_selector('#app > div > div > div > div.timing-screen-header > div.flag-status.flag-status-caution')):
            nl.set_color(YELLOW)
            time.sleep(10)
        elif (driver.find_elements_by_css_selector('#app > div > div > div > div.timing-screen-header > div.flag-status.flag-status-red')):
            nl.set_color(RED)
            time.sleep(10)
        elif (driver.find_elements_by_css_selector('#app > div > div > div > div.timing-screen-header > div.flag-status.flag-status-chequered')):
            nl.set_color(WHITE)
            time.sleep(60)
            quit()
        else:
            print("No Status")
            time.sleep(10)

if __name__ == "__main__":
    main()