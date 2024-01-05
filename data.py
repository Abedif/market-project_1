import sqlite3

class Database :
    def __init__(self , db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(''' create table if not exists market
                          (id integer primary key , name text , buy integer , sale integer , number integer) ''')
        self.con.commit()


    
    def insert_table(self , name , buy , sale , number):
        self.cur.execute('''insert into market values (Null , ? , ? , ? ,?
                         )''' , (name , buy , sale , number))
        self.con.commit()
        
        print(self.cur.rowcount , 'record inserted!')
        print('last ID is : ' , self.cur.lastrowid)
        
        
    def select_record(self):
        self.cur.execute('select * from market')
        record =  self.cur.fetchall()
        return record
    
    def delete_record (self , id):
        self.cur.execute('delete from market where id = ? ' , (id ,) )
        self.con.commit()
        
        
    def update_records (self , id , name , buy , sale , number ):
        self.cur.execute('''update market set name = ? , buy = ? , sale = ?
                         , number = ? where id = ? ''' , (name, buy , sale , number , id ))
                         
        self.con.commit()
        
        
    def search_records(self , name):
        self.cur.execute('select * from market where name = ? ' , (name,) )
        row = self.cur.fetchone()
        return row
    
    