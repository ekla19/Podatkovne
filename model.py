import baza_mesta
import sqlite3

conn = sqlite3.connect("baza_potovanj.sqlite3")

class Model:
    def dobi_vse_drzave(self):
        with conn:
            cur = conn.execute("""
            SELECT * FROM evropske_drzave
            """)

            return cur.fetchall()

#pripravimo vse tabele v primeru, da še ne obstajajo