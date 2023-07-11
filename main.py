from crawler import main
from db.database import initialize
import logging

logging.basicConfig(
    filename='logs.log',
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    filemode='w',
    encoding='utf-8',
    level=logging.INFO,
)

initialize()
main()
