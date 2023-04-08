#От таблицы Состав отказались, согласованно с преподавателем


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
    zayav.execute("UPDATE store_statements SET date_zayav = '2022-1-29' WHERE id_zayav = 40")


with sq.connect('Opt. base') as kol:
    kol_tov = kol.cursor()
    kol_tov.execute("""CREATE TABLE IF NOT EXISTS number_of_goods_in_stock (
        id_kol_tov INTEGER PRIMARY KEY,
        kol_vo INTEGER,
        id_tov INTEGER,
        FOREIGN KEY (id_tov)  REFERENCES goods (id_tov)
    )""")
    #kol.execute("INSERT INTO number_of_goods_in_stock VALUES (30, 600, 10)")



#1 ars.execute("SELECT name_tov, opis FROM goods")
#2 ars.execute("SELECT nazv_mag, address FROM shop")
#3 ars.execute("SELECT id_zayav, date_zayav FROM store_statements")
#4 ars.execute("SELECT id_tov, kol_vo FROM number_of_goods_in_stock")
#5 ars.execute("SELECT id_tov, kol_vo FROM number_of_goods_in_stock ORDER BY kol_vo DESC")
#6 ars.execute("SELECT id_zayav, id_tov FROM compound")
#7 ars.execute("SELECT * FROM number_of_goods_in_stock WHERE kol_vo < 5000")
#8 ars.execute("SELECT * FROM store_statements WHERE (date_zayav BETWEEN '2022.8.15' AND '2022.11.30')")
#9 -


resolt = ars.fetchall()
print(resolt)