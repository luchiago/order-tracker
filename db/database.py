import logging
import sqlite3
from typing import Optional, Tuple

con = sqlite3.connect("status.db")
cur = con.cursor()


def initialize():
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS status(
            date TEXT NOT NULL,
            status TEXT
        )
    """
    )
    con.commit()


def insert_latest_status(status: Tuple) -> None:
    logging.info(f"Inserting status {status}")

    cur.execute("INSERT INTO status VALUES(?, ?)", status)
    con.commit()

    logging.info("Successfully inserted status")


def fetch_latest_status() -> Optional[Tuple]:
    logging.info("Fetching latest status")

    res = cur.execute("SELECT * FROM status")
    return res.fetchone()
