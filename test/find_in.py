import sqlite3 as sq
import time
from datetime import datetime

testname = 'kazu'
in_out = 0

def test(element):
    sum_item = 0
    for el in element:
        sum_item += int(el[4])

        d = datetime.strptime(str(el[5]), "%Y.%m.%d %H:%M:%S")
        ts_d = time.mktime(d.timetuple())

        print(str(el[0]) + " - " + str(el[3]) + " - " + str(el[4]) + " - " + str(el[5]) + " - " + str(int(ts_d)))
    return sum_item

with sq.connect("../db/wallet.db") as con:
    date = datetime.today().strftime("%Y.%m.%d %H:%M:%S")
    datetime = datetime.strptime(str(date), "%Y.%m.%d %H:%M:%S")
    ts_date = time.mktime(datetime.timetuple())

    cur = con.cursor()
    cur.execute(f"SELECT rowid, * FROM wallet_info WHERE wallet_in_out = '{in_out}'") # ORDER BY `rowid` DESC LIMIT 10
    item = cur.fetchall()

    item_len = len(item)

    sum_item = test(item)

    print("\n" + str(sum_item))
    print(len(item))





