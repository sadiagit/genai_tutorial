import sqlite3
from zipfile import Path
from pathlib import Path

def get_db_connection(db_path='db/genia.db'):
    BASE_DIR = Path(__file__).resolve().parent
    DB_PATH = BASE_DIR / "genia.db"
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn