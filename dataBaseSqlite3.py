
import sqlite3
def  main():
    db = sqlite3.connect("info.db")
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists  Admin(Name text,age int)")
    db.execute("insert into Admin (Name,age) values (? , ?)", ("zaid", 25))
    db.execute("insert into Admin (Name,age) values (? , ?)", ("saad", 12))

    db.execute("delete from Admin where Name='saad' ")
    db.execute("update  Admin set age=28 where Name='zaid' ")
    db.commit()
    c = db.execute("select * from Admin")
    for row in c:
        print("name : {} , age : {} ".format(row["Name"],row["age"]))

if __name__ == '__main__':main()
