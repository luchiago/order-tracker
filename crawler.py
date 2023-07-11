import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging

from db.database import fetch_latest_status, insert_latest_status

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

    sleep(2)

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


def extract_info() -> None:
    driver.get(ORDER_URL)

    sleep(2)

    table_element = driver.find_elements(By.CLASS_NAME, 'table')[-1]
    table_element = table_element.find_element(By.XPATH, './/tbody')

    rows = table_element.find_elements(By.XPATH, './/tr')
    latest_row = rows[-1]

    cells = latest_row.find_elements(By.XPATH, './/td')[:2]
    date, status = [cell.text for cell in cells]

    latest_date, latest_status = '', ''
    latest = fetch_latest_status()

    if latest is not None:
        latest_date, latest_status = latest

    if latest_date != date or latest_status != status:
        logging.info(f'New status: {date} {status}')

        insert_latest_status((date, status))
    else:
        logging.info('No new updates')

    logging.info('Extraction completed')


def main():
    logging.info(f'Performing login for account {EMAIL}')
    login()

    logging.info(f'Extracting info for order {ORDER_ID}')
    extract_info()

    driver.quit()
