import logging
import os
import time

import schedule
from dotenv import load_dotenv

from crawler import main
from db.database import initialize

load_dotenv()

logging.basicConfig(
    filename="logs.log",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filemode="w",
    encoding="utf-8",
    level=logging.INFO,
)

IN_DOCKER = bool(int(os.getenv("IN_DOCKER")))


def run():
    initialize()
    main()


def run_scheduled():
    schedule.every().day.at("10:00", "America/Sao_Paulo").do(run)
    schedule.every().day.at("18:00", "America/Sao_Paulo").do(run)

    while True:
        schedule.run_pending()
        time.sleep(1)


if IN_DOCKER:
    run_scheduled()
else:
    run()
