import json
import logging
import sqlite3
from contextmanager import conn_context

DB_PATH = 'data/sql_app.db'


def load_data(sqlite_cursor: sqlite3.Cursor):

    #sqlite_cursor.execute('CREATE TABLE wer (name TEXT, description TEXT)')

    with open('flowers.json', 'r') as file:
        data = json.load(file)
        for line in data:
            sqlite_cursor.execute('INSERT INTO flower (name, description) VALUES (?, ?)', (line['name'], line['description']))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    with conn_context(DB_PATH) as sqlite_cursor:
        load_data(sqlite_cursor)
