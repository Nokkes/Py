import sqlite3
db = sqlite3.connect('c:\sickrage\data\sickrage.db')
cursor = db.cursor()

cursor.execute(''' SELECT * from info ''')

db.close