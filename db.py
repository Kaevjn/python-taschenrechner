import sqlite3

DB_FILE = "history.db"

def create_table():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT NOT NULL,
    num1 REAL NOT NULL,
    num2 REAL NOT NULL,
    result REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

    def save_calculation(operation, num1, num2, result):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''
        INSERT INTO calculations (operation, num1, num2, result)
        VALUES (?, ?, ?, ?)
    ''', (operation, num1, num2, result))
    conn.commit()
    conn.close()

def get_last_calculations(limit=10):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT operation, num1, num2, result
        FROM calculations
        ORDER BY id DESC
        LIMIT ?
    ''', (limit,))
    rows = c.fetchall()
    conn.close()
    return rows