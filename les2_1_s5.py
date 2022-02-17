import math
import time

from selenium import webdriver

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    inputField = browser.find_element_by_id('answer')
    inputField.send_keys(y)

    check = browser.find_element_by_id('robotCheckbox')
    check.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
