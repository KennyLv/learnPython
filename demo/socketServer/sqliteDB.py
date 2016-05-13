import sqlite3

db_path = "D:\\HBuild_WorkSpace\\learnPython\\test.db"

#插入
def addCategory(categroy_name):
    conn_insert = sqlite3.connect(db_path)
    c_insert    = conn_insert.cursor()
    # execute "INSERT" 
    c_insert.execute("INSERT INTO category VALUES (?, ?)", [ None ,categroy_name])
    # using the placeholder
    #SQL语句中的参数，使用"?"作为替代符号，并在后面的参数中给出具体值。
    #这里不能用Python的格式化字符串，如"%s"，因为这一用法容易受到SQL注入攻击。
    #c_insert.execute("INSERT INTO category VALUES (?, ?, ?)", ['2', '2', 'computer'] )
    # execute multiple commands
    #c_insert.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
    conn_insert.commit()
    conn_insert.close()

#删除
def deleteCategroyById(category_id):
    conn_delete = sqlite3.connect(db_path)
    c_delete = conn_delete.cursor()
    c_delete.execute('DELETE FROM category WHERE id=?', [category_id])
    conn_delete.commit()
    conn_delete.close()
    
    
#插入
def addBook(book_name, book_price, cat_id):
    conn_insert = sqlite3.connect(db_path)
    c_insert    = conn_insert.cursor()
    # execute "INSERT" 
    c_insert.execute("INSERT INTO book VALUES (?, ?, ?, ?)", [None, book_name, book_price, cat_id])
    # using the placeholder
    #SQL语句中的参数，使用"?"作为替代符号，并在后面的参数中给出具体值。
    #这里不能用Python的格式化字符串，如"%s"，因为这一用法容易受到SQL注入攻击。
    #c_insert.execute("INSERT INTO category VALUES (?, ?, ?)", ['2', '2', 'computer'] )
    # execute multiple commands
    #c_insert.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
    conn_insert.commit()
    conn_insert.close()

'''
#插入
def addBooks(books):
    conn_insert = sqlite3.connect(db_path)
    c_insert    = conn_insert.cursor()
    books = [(1, 1, 'Cook Recipe', 3.12, 1),
                (2, 3, 'Python Intro', 17.5, 2),
                (3, 2, 'OS Intro', 13.6, 2),
               ]
    # execute multiple commands
    c_insert.executemany('INSERT INTO book VALUES (?, ?, ?)', books)
    conn_insert.commit()
    conn_insert.close()
 '''
    
#删除
def deleteBookById(book_id):
    conn_delete = sqlite3.connect(db_path)
    c_delete = conn_delete.cursor()
    c_delete.execute('DELETE FROM book WHERE id=?', [book_id])
    #c_delete.execute("DROP TABLE if exists staff")
    #c_delete.execute('DROP TABLE book')
    conn_delete.commit()
    conn_delete.close()
    
'''
#更新
def update(a,b,c,d):
    conn_update = sqlite3.connect(db_path)
    c_update = conn_update.cursor()
    c_update.execute('UPDATE book SET price=? WHERE id=?', (1000, 1))
    conn_update.commit()
    conn_update.close()
'''

#查询
def queryAll():
    conn_query = sqlite3.connect(db_path)
    c_query = conn_query.cursor()
    # retrieve one record
    c_query.execute('SELECT * FROM book left join category on book.category=category.id')
    #print(c_query.fetchone())
    #print(c_query.fetchone())
    # retrieve all records as a list
    #c_query.execute('SELECT * FROM book WHERE book.category=1  ORDER BY sort')
    rows = c_query.fetchall()
    conn_query.close()
    return rows

#创建数据库
def createDB():
    conn_create = sqlite3.connect(db_path)
    c_create = conn_create.cursor()
    # create tables
    #对于SQLite， 主键数据类型为 int 类型，插入的时候，不传入数据， 就是默认为自动递增处理。
    c_create.execute('''CREATE TABLE IF NOT EXISTS category 
          (id INTEGER PRIMARY KEY AutoIncrement, name text)''')
    c_create.execute('''CREATE TABLE IF NOT EXISTS book 
          (id INTEGER PRIMARY KEY AutoIncrement, 
           name text, 
           price real, 
           category int,
           FOREIGN KEY (category) REFERENCES category(id))''')
    # save the changes and close the connection with the database
    conn_create.commit()
    conn_create.close()
    
if __name__ == '__main__': 
    #createDB()
    #addBook('Start on Python', 33.5, 3)
    #addCategory('Computer')
    #deleteCategroyById(4)
    for row in queryAll():
        print(row)