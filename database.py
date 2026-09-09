import sqlite3
pricesDB = "prices.db"

with sqlite3.connect(pricesDB) as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS prices (city TEXT PRIMARY KEY, price REAL)')
    conn.commit()