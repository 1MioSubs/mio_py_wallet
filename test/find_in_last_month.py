import sqlite3 as sq
import time
from datetime import datetime

testname = 'kazu'
in_out = 0

with sq.connect("../db/wallet.db") as con:
    date = datetime.today().strftime("%Y.%m.%d %H:%M:%S")
    datetime = datetime.strptime(str(date), "%Y.%m.%d %H:%M:%S")
    ts_date = int(time.mktime(datetime.timetuple()))

    cur = con.cursor()
    cur.execute(f"SELECT rowid, * FROM wallet_info WHERE wallet_in_out = '{in_out}'") # ORDER BY `rowid` DESC LIMIT 10
    item = cur.fetchall()

    sum_item = 0
    item_len = len(item)

    for el in item:

        d = datetime.strptime(str(el[5]), "%Y.%m.%d %H:%M:%S")
        ts_d = int(time.mktime(d.timetuple()))

        if ts_d > ts_date - 604800: #2592000:
            sum_item += int(el[4])
            print(str(el[0]) + " - " + str(el[3]) + " - " + str(el[4]) + " - " + str(el[5]) + " - " + str(int(ts_d)))

    print("\n" + str(sum_item))
    print(len(item))





