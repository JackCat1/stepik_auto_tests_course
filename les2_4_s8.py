import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()

try:
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'book'))
    )
    button.click()

    x_value = browser.find_element_by_id('input_value')
    res = math.log(abs(12 * math.sin(int(x_value.text))))

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(res)

    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()
finally:
    time.sleep(30)
    browser.quit()
