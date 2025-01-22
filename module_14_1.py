import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# for i in range(1, 11):
#     n = 10
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', str(n*i), 1000))
#
# cursor.execute('UPDATE Users SET balance = ? WHERE (id - 1) % 2 = ?', (500, 0))
# cursor.execute('DELETE FROM Users WHERE (id - 1) % 3 = 0')
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
# users = cursor.fetchall()
# for user in users:
#     username, email, age, balance = user
#     print(f'Имя:{username}, Почта: {email}, Возраст: {age}, Баланс: {balance}')
cursor.execute('DELETE FROM Users WHERE id = 6')
cursor.execute('SELECT COUNT(*) FROM Users')
all_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
balance_sum = cursor.fetchone()[0]

cursor.execute('SELECT AVG(balance) FROM Users')
balance_avg = cursor.fetchone()[0]
print(balance_avg)

connection.commit()
connection.close()