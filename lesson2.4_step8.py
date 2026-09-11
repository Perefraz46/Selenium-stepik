from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from calc_math import calc
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    order_text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'$100')
    )

    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    input_value = browser.find_element(By.ID, 'input_value').text
    total = calc(int(input_value))

    total_input = browser.find_element(By.ID, 'answer')
    total_input.send_keys(total)

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

finally:
    time.sleep(7)
    browser.quit()
