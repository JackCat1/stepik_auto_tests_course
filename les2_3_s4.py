import time
import math

from selenium import webdriver

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()

try:
    browser.get(link)

    button_start = browser.find_element_by_css_selector('button[type="submit"]')
    button_start.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    x_value = browser.find_element_by_id('input_value')
    res = math.log(abs(12 * math.sin(int(x_value.text))))

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(res)

    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()
finally:
    time.sleep(30)
    browser.quit()
