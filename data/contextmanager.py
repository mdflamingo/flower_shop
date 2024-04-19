import logging
import sqlite3
from contextlib import contextmanager


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        logging.info("Creating connection")
        yield conn.cursor()
    finally:
        logging.info("Closing connection")
        conn.close()

