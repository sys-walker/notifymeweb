#!/usr/bin/env python3
import os
import signal
import sys
from time import strftime, sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def signal_handler(signal, frame):
    if WEBDRIVER is not None:
        WEBDRIVER.quit()
    sys.exit(0)


def set_webdriver(driver):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(executable_path=os.path.abspath("geckodriver"), options=options)
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    WEBDRIVER = None
    WEBDRIVER = set_webdriver(WEBDRIVER)
    signal.signal(signal.SIGINT, signal_handler)

    print("Please Wait Starting Notify Me When is Up")

    try:

        TAIL = input("Enter URL > ")
        URL_WEB = "https://downforeveryoneorjustme.com/" + (TAIL)
        if URL_WEB == "https://downforeveryoneorjustme.com/":
            raise Exception("No website to check status")
        print("checking every 10 sec " + URL_WEB)
        OFFLINE = True
        ONLINE = True
        ISSUE = 5
        while True:
            WEBDRIVER.get(URL_WEB)

            if WEBDRIVER.current_url == "https://downforeveryoneorjustme.com/error":
                raise Exception("This website doesn't exists")
            array = WEBDRIVER.find_elements_by_class_name("is-size-6")

            if len(array) != 0:

                t = strftime("%Y-%m-%d %H:%M:%S")

                if "It's not just you!" in array[0].text:
                    ISSUE = 5
                    print(t[11:], "-->", array[0].text)

                    if OFFLINE:
                        os.system('notify-send  "-i" error "Notify Me!" "{0} "'
                                  .format(array[0].text))
                        os.system('espeak -ven-us+f4 -s140 -a 500 "{0}"'.format(array[0].text))
                    OFFLINE = False
                    ONLINE = True
                elif "It's just you" in array[0].text:
                    ISSUE = 5
                    print(t[11:], "-->", array[0].text)
                    if ONLINE:
                        os.system('notify-send  "-i" info "Notify Me!" "{0} "'
                                  .format(array[0].text))
                        os.system('espeak -ven-us+f4 -s140 -a 500 "{0}"'.format(array[0].text))
                    ONLINE = False
                    OFFLINE = True

                else:
                    if ISSUE > 10:
                        os.system('notify-send  "-i" critical "Notify Me!'
                                  '" I have problems with downforeveryoneorjustme keep calm  "')
                    sleep(ISSUE)
                    ISSUE = ISSUE + 2

                sleep(2)
            else:
                raise Exception("Element is missing")
    except Exception as error:
        print("Panic exit", error)
        if WEBDRIVER is not None:
            WEBDRIVER.quit()
        sys.exit(1)
