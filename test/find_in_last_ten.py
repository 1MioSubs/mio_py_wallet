import sqlite3 as sq
import time
from datetime import datetime

in_out = 1

with sq.connect("../db/wallet.db") as con:

    cur = con.cursor()
    cur.execute(f"SELECT rowid, * FROM wallet_info WHERE wallet_in_out = '{in_out}'")  # ORDER BY `rowid` DESC LIMIT 10
    item = cur.fetchall()

    sum_item = 0
    item_len = len(item)
    item_prob = 0

    for el in item:
        item_prob += 1

        d = datetime.strptime(str(el[5]), "%Y.%m.%d %H:%M:%S")
        ts_d = time.mktime(d.timetuple())

        if item_prob > item_len - 10:
            sum_item += int(el[4])
            print(str(el[0]) + " - " + str(el[3]) + " - " + str(el[4]) + " - " + str(el[5]) + " - " + str(int(ts_d)))

    print("\n" + str(sum_item))
    print(len(item))





