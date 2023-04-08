import sqlite3 as sq
from info import tovars_info
from info import zayav_info


with sq.connect('Opt. base') as tov:
    ars = tov.cursor()
    ars.execute("""CREATE TABLE IF NOT EXISTS goods (
        id_tov INTEGER PRIMARY KEY,
        name_tov VARCHAR,
        opis VARCHAR,
        ed_ismer VARCHAR
    )""")
    #ars.execute("INSERT INTO goods VALUES (9, 'Мука', 'Прордукты', 'Грамм')")




with sq.connect('Opt. base') as mag:
    azin = mag.cursor()
    azin.execute("""CREATE TABLE IF NOT EXISTS shop (
        id_mag INTEGER PRIMARY KEY,
        nazv_mag VARCHAR,
        address VARCHAR,
        phone_number VARCHAR
    )""")
    #mag.execute("INSERT INTO shop VALUES (20, 'Пятёрочка', 'ул. Крышкина', '+7 999 103 56 34')")

with sq.connect('Opt. base') as zayav:
    magaz = zayav.cursor()
    magaz.execute("""CREATE TABLE IF NOT EXISTS store_statements (
        id_zayav INTEGER PRIMARY KEY,
        date_zayav DATE,
        id_mag INTEGER,
        FOREIGN KEY (id_mag)  REFERENCES shop (id_mag)
    )""")
    #zayav.execute("INSERT INTO store_statements VALUES (40, '2023.1.29', 17)")


with sq.connect('Opt. base') as kol:
    kol_tov = kol.cursor()
    kol_tov.execute("""CREATE TABLE IF NOT EXISTS number_of_goods_in_stock (
        id_kol_tov INTEGER PRIMARY KEY,
        kol_vo INTEGER,
        id_tov INTEGER,
        FOREIGN KEY (id_tov)  REFERENCES goods (id_tov)
    )""")
    #kol.execute("INSERT INTO number_of_goods_in_stock VALUES (30, 600, 10)")

with sq.connect('Opt. base') as coc:
    tav = coc.cursor()
    tav.execute("""CREATE TABLE IF NOT EXISTS compound (
        id_coc INTEGER PRIMARY KEY,
        kol_vo INTEGER,
        id_zayav INTEGER,
        id_tov INTEGER,
        FOREIGN KEY (id_zayav)  REFERENCES store_statements (id_zayav),
        FOREIGN KEY (id_tov)  REFERENCES goods (id_tov)
    )""")
    coc.execute("INSERT INTO compound VALUES (41, 40, 33, 7)")