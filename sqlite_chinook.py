import sqlite3

## connect to sqllite
connection=sqlite3.connect("chinook.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()


data=cursor.execute('''Select * from tracks''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
