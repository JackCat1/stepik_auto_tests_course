import math
import time

from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)

    img = browser.find_element_by_tag_name('img')
    x = img.get_attribute('valuex')
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
