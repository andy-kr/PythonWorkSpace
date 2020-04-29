import sqlite3
class DBHandle:
    def __init__(self):
        db = sqlite3.connect('product.db')
        sql ='create table if not exists product(jepoom varchar(20),pcount int, pdate date)'
        db.execute(sql)
        db.close()
    def insertData(self,jepoom, pcnt, pdate):
        db = sqlite3.connect('product.db')
        sql ='insert into product values(?,?,?)'
        db.execute(sql, (jepoom,pcnt,pdate))
        db.commit()
        db.close()
    def selectData(self):
        db = sqlite3.connect('product.db')
        sql = 'select * from product'
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        db.close()
        return data
