import csv
import sqlite3 as sq

testname = 'kazu'

with sq.connect("../db/wallet.db") as con:
    cur = con.cursor()
    cur.execute(f"INSERT INTO user_info (user_name) VALUES ('{testname}')")


