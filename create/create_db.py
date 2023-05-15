import csv
import sqlite3 as sq

with sq.connect("../db/wallet.db") as con:
    cur = con.cursor()

    #Создание таблици запросов инвойсов
    cur.execute("DROP TABLE IF EXISTS wallet_info")
    cur.execute("""CREATE TABLE IF NOT EXISTS wallet_info (
        wallet_in_out TEXT NOT NULL,
        wallet_in_out_id TEXT NOT NULL,
        wallet_in_out_text TEXT NOT NULL,
        sum TEXT NOT NULL,
        date TEXT NOT NULL
        )""")
# wallet_user TEXT NOT NULL

    #Создание таблици админов и запись основных
    cur.execute("DROP TABLE IF EXISTS user_info")
    cur.execute("""CREATE TABLE IF NOT EXISTS user_info (
            user_name TEXT NOT NULL
            )""")

    with open("../db/db_csv/user.csv", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            test1 = row["user_name"]
            cur.execute(f"INSERT INTO user_info (user_name) VALUES ('{test1}')")


