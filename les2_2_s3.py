import time
from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()


try:
    browser.get(link)

    x1_element = browser.find_element_by_id('num1')
    x1 = int(x1_element.text)
    x2_element = browser.find_element_by_id('num2')
    x2 = int(x2_element.text)

    res = x1 + x2

    select = browser.find_element_by_id('dropdown')
    select.click()

    option = browser.find_element_by_css_selector('[value="'+str(res)+'"]')
    option.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
