import logging
import os
import time

import schedule
from dotenv import load_dotenv

from crawler import main
from db.database import initialize

load_dotenv()

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    encoding="utf-8",
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)

IN_DOCKER = bool(int(os.getenv("IN_DOCKER")))


def run():
    logging.info('Starting the crawling process')
    initialize()
    main()


def run_scheduled():
    schedule.every().day.at("10:00", "America/Sao_Paulo").do(run)
    schedule.every().day.at("18:00", "America/Sao_Paulo").do(run)

    while True:
        schedule.run_pending()
        time.sleep(1)

logging.info('Starting the main script')

if not IN_DOCKER:
    logging.info('Running on scheduled mode')
    run_scheduled()
else:
    logging.info('Running locally')
    run()
