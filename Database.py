import pandas as pd
import sqlite3


class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS dane (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data TEXT,
                        opis TEXT,
                        kategoria TEXT,
                        kwota REAL
                    )
                    """)
        self.conn.commit()

    def save_to_db(self, dane, table_name='dane'):

        self.conn.executemany("""
            INSERT INTO dane(data, opis, kategoria, kwota) VALUES (?, ?, ?, ?)
        """, dane.to_records(index=False))
        self.conn.commit()

    def fetch_expenses(self, month, year, table_name='dane'):
        self.cursor.execute(f"""
            SELECT * FROM {table_name} 
            WHERE strftime('%m', data)='{month}' AND strftime('%Y', data)='{year}' 
            ORDER BY data DESC
        """)
        return self.cursor.fetchall()

    def update_db(self, indeks, column, value):
        self.cursor.execute(f"UPDATE dane SET {column} = ? WHERE id = ?", (value, indeks))
        self.conn.commit()

    def delete_row(self, row_id):
        self.cursor.execute("DELETE FROM dane WHERE id = ?", (row_id,))
        self.conn.commit()


    def fetch_saldo(self, month, year):
        self.cursor.execute(f"""
            SELECT sum(kwota) FROM dane
            WHERE strftime('%m', data)='{month}' AND strftime('%Y', data)='{year}' AND kategoria NOT IN('Bez kategorii','Nieistotne','Mieszkanie','Nieistotne - inne')
        """)
        rows = self.cursor.fetchall()
        return rows[0][0] if rows else 0

    def fetch_wydatki(self, month, year):
        self.cursor.execute(f"""
            SELECT sum(kwota) FROM dane
            WHERE strftime('%m', data)='{month}' AND strftime('%Y', data)='{year}' AND kategoria NOT IN('Bez kategorii','Wpływy - inne','Wpływy','Mieszkanie','Wynagrodzenie','Rodzice','Nieistotne','Nieistotne - inne')
        """)
        rows = self.cursor.fetchall()
        return rows[0][0] if rows else 0

    def fetch_wplywy(self, month, year):
        self.cursor.execute(f"""
            SELECT sum(kwota) FROM dane
            WHERE strftime('%m', data)='{month}' AND strftime('%Y', data)='{year}' AND kategoria IN('Wpływy - inne','Wpływy','Rodzice','Wynagrodzenie')
        """)
        rows = self.cursor.fetchall()
        return rows[0][0] if rows else 0
    
    def fetch_wplywy1(self, month, year):
        self.cursor.execute(f"""
            SELECT kategoria,sum(kwota) FROM dane
            WHERE strftime('%m', data)='{month}' AND strftime('%Y', data)='{year}' AND kategoria IN('Wpływy - inne','Wpływy','Rodzice','Wynagrodzenie')
            GROUP BY kategoria
            ORDER BY sum(kwota) DESC
        """)
        rows = self.cursor.fetchall()
        return rows
    
    def fetch_kategorie(self, month, year):
        self.cursor.execute(f"""
            SELECT kategoria, sum(kwota) FROM dane
            WHERE strftime('%m', data)='{month}' AND strftime('%Y', data)='{year}' AND kategoria NOT IN('Bez kategorii','Wpływy - inne','Wpływy','Wynagrodzenie','Rodzice','Nieistotne','Mieszkanie','Nieistotne - inne')
            GROUP BY kategoria
            ORDER BY sum(kwota) DESC
        """)
        rows = self.cursor.fetchall()
        return rows

    def fetch_previous_months(self, month, year):
        self.cursor.execute(f"""
            SELECT DISTINCT strftime('%m', data) as month, strftime('%Y', data) as year FROM dane
            WHERE (strftime('%Y', data) < '{year}') OR (strftime('%Y', data) = '{year}' AND strftime('%m', data) < '{month}')
            ORDER BY year DESC, month DESC
        """)
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()