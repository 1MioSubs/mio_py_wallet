from random import randint
import sqlite3 as sq
import datetime
from time import sleep


i = 0
while i < 15:
    i += 1
    wallet_in_out = int(randint(0, 1))
    wallet_in_out_id = int(randint(1, 6))

    if wallet_in_out_id == 1:
        wallet_in_out_text = 'крипта'
    elif wallet_in_out_id == 2:
        wallet_in_out_text = 'таврия'
    elif wallet_in_out_id == 3:
        wallet_in_out_text = 'интернет'
    elif wallet_in_out_id == 4:
        wallet_in_out_text = 'работа'
    elif wallet_in_out_id == 5:
        wallet_in_out_text = 'разное'
    elif wallet_in_out_id == 6:
        wallet_in_out_text = 'сайт'

    sum_in_out = int(randint(50, 1000))
    # date = datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S")
    # 2023.04.1 10:00:00
    date = "2023.05." + str(i) + " 10:00:00"
    with sq.connect("../db/wallet.db") as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO wallet_info (wallet_in_out, wallet_in_out_id, wallet_in_out_text, sum, date) VALUES ('{wallet_in_out}', '{wallet_in_out_id}', '{wallet_in_out_text}', '{sum_in_out}', '{date}')")




