# By Vamei
import sqlite3

db_path = "D:\\HBuild_WorkSpace\\learnPython\\src\\test.db"

#创建数据库
# test.db is a file in the working directory.
conn_create = sqlite3.connect(db_path)
c_create = conn_create.cursor()
# create tables
c_create.execute('''CREATE TABLE IF NOT EXISTS category 
      (id int primary key, sort int, name text)''')
c_create.execute('''CREATE TABLE IF NOT EXISTS book 
      (id int primary key, 
       sort int, 
       name text, 
       price real, 
       category int,
       FOREIGN KEY (category) REFERENCES category(id))''')
# save the changes and close the connection with the database
conn_create.commit()
conn_create.close()

#删除
conn_delete = sqlite3.connect(db_path)
c_delete = conn_delete.cursor()
c_delete.execute('DELETE FROM category WHERE id=1')
#c_delete.execute("DROP TABLE if exists staff")
#c_delete.execute('DROP TABLE book')
conn_delete.commit()
conn_delete.close()

#插入数据
conn_insert = sqlite3.connect(db_path)
c_insert    = conn_insert.cursor()

books = [(1, 1, 'Cook Recipe', 3.12, 1),
            (2, 3, 'Python Intro', 17.5, 2),
            (3, 2, 'OS Intro', 13.6, 2),
           ]

# execute "INSERT" 
c_insert.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")
# using the placeholder
#SQL语句中的参数，使用"?"作为替代符号，并在后面的参数中给出具体值。
#这里不能用Python的格式化字符串，如"%s"，因为这一用法容易受到SQL注入攻击。
c_insert.execute("INSERT INTO category VALUES (?, ?, ?)", ['2', '2', 'computer'] )
# execute multiple commands
c_insert.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
conn_insert.commit()
conn_insert.close()

#更新
conn_update = sqlite3.connect(db_path)
c_update = conn_update.cursor()
c_update.execute('UPDATE book SET price=? WHERE id=?', (1000, 1))
conn_update.commit()
conn_update.close()

#查询
conn_query = sqlite3.connect(db_path)
c_query = conn_query.cursor()
# retrieve one record
c_query.execute('SELECT name FROM category ORDER BY sort')
print(c_query.fetchone())
print(c_query.fetchone())

# retrieve all records as a list
c_query.execute('SELECT * FROM book WHERE book.category=1')
print(c_query.fetchall())

# iterate through the records
#在执行查询语句后，Python将返回一个循环器，包含有查询获得的多个记录。
#你循环读取，也可以使用sqlite3提供的fetchone()和fetchall()方法读取记录：
for row in c_query.execute('SELECT name, price FROM book ORDER BY sort'):
    print(row)


