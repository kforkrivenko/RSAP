import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()


cursor.execute('''SELECT message FROM dima_yulya_message''')
enter = cursor.fetchall()
print(enter)