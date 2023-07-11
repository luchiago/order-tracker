import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging

load_dotenv()

ORDER_ID=os.getenv('ORDER_ID')
ORDER_URL=f"{os.getenv('ORDER_URL')}{ORDER_ID}"
LOGIN_URL=os.getenv('LOGIN_URL')
EMAIL=os.getenv('EMAIL')
PASSWORD=os.getenv('PASSWORD')

options = Options()
options.headless = bool(int(os.getenv('IN_DOCKER')))
driver = webdriver.Firefox(options=options)

def login() -> None:
    driver.get(LOGIN_URL)

    email_input = driver.find_element(By.ID, 'input-email')
    password_input = driver.find_element(By.ID, 'input-password')

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)

    submit_button = driver.find_element(
        By.XPATH,
        '/html/body/div[3]/div/div/div/div/div/div[2]/div/form/input[1]',
    )

    submit_button.click()

    logging.info(f'Login completed')

    sleep(2)

def extract_info() -> None:
    driver.get(ORDER_URL)

    table_element = driver.find_element(
        By.XPATH,
        '/html/body/div[2]/div/div/div/div/table[3]/tbody',
    )

    rows = table_element.find_elements(By.XPATH, './/tr')

    statuses = []

    for row in rows:
        cells = row.find_elements(By.XPATH, './/td')[:2]
        status_and_date = [cell.text for cell in cells]

        statuses.append(status_and_date)

    logging.info('Extraction completed')


def main():
    logging.info(f'Performing login for account {EMAIL}')
    login()

    logging.info(f'Extracting info for order {ORDER_ID}')
    extract_info()

    driver.quit()
