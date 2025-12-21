import streamlit as st
import pandas as pd
import sqlite3
import datetime

conn = sqlite3.connect('baza1.db')
c = conn.cursor()

# --- 🛠️ WYMUSZENIE POPRAWNEJ STRUKTURY BAZY ---
# To sprawi, że ID będzie się samo dodawać (1, 2, 3...)
c.execute('''
    CREATE TABLE IF NOT EXISTS dane (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        kategoria TEXT,
        opis TEXT,
        kwota REAL
    )
''')

c.execute('SELECT * FROM dane')
row = c.fetchone()
for i in row:
    print(i)
else:
    print("Brak wiersza o id=1")
conn.commit()
conn.close()
