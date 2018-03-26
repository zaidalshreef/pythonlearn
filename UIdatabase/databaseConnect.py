import sqlite3

class DBConnect:
    def __init__(self):
        self.DB=sqlite3.connect("Resrvation.db")
        self.DB.row_factory=sqlite3.Row
        self.DB.execute("create table if not exists Ticket(ID integer primary key autoincrement,Name text,Gender text, Comment text)")
        self.DB.commit()

    def add(self,name,gender,comment):
        self.DB.execute("insert into Ticket(Name,Gender,Comment) values(:Name,:Gender,:Comment)",{'Name':name,'Gender':gender,'Comment':comment})
        self.DB.commit()
        return "requst is submited"

    def ListRequst(self):
        cursor=self.DB.execute("Select * from Ticket")
        return cursor


    def deleteRecord(self,id):
        self.DB.execute("delete from Ticket where ID=:ID",{'ID':id})
        self.DB.commit()
        return "Record is deleted"

    def UpdateRecord(self,id,comment):
        self.DB.execute("update Ticket set Comment=:Comment where ID=:ID ",{'Comment':comment,'ID':id})
        self.DB.commit()
        return "Record is updated"


    


