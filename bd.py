import sqlite3
 
conn = sqlite3.connect('bibla.db') # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
 
# Создание таблицы
#cursor.execute("CREATE TABLE books(inv INTEGER PRIMARY KEY, name text, jenre text, ypub integer, author text, izd text, num integer)")  
cursor.execute("CREATE TABLE ticket(fam text, name text, otch text, numt integer, datevyd text, datevoz text, inv integer)")  
#cursor.execute("DROP TABLE ticket")
#cursor.execute("INSERT INTO books (name, jenre, ypub, author, izd, num) VALUES ('kik', 'kul',2004,'pipch','chiki',2)")
conn.commit()
cursor.close()