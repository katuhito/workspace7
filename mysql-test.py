import MySQLdb

# MySQLに接続する
conn = MySQLdb.connect(
    user='root',
    password='test-password',
    host='localhost',
    db='test'
)

# カーソルを取得する
cur = conn.cursor()

# テーブルを作成する
cur.execute('DROP TABLE IF EXISTS items')
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
    ''')

# データを挿入する
data = [('Banana', 300), ('Mango', 640), ('Kiwi', 280)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES(%s,%s)", i)

# データを抽出する
cur.execute("select * from items")
for row in cur.fetchall():
    print(row)
    