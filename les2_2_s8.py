import os.path
import time

from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

browser = webdriver.Chrome()

try:
    browser.get(link)

    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys('Ivan')

    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys('Ivanov')

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('admin@mail.ru')

    file = browser.find_element_by_css_selector('[name="file"]')
    file.send_keys(file_path)

    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()
finally:
    time.sleep(30)
    browser.quit()
