
#dounload sqlite (create new db and import db file ("student"))

import sqlite3

#my module to print msg 
import module

#enter databasename and filename code
"""filename=input("Enter DataBase Name : ")
tablename=input("Enter Table Name : ")
filename=filename+".sqlite3"      """

#take user input
name=input("Enter your Name : ")
Age=input("Enter your Age : ")
college=input("Enter your College Name : ")

#open Database
f=open("db.sqlite3","a")

#connect to database
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
#create table 
#cur.execute("CREATE TABLE "+tablenamr+"(name text, Age text, college text)")

#insert entered data to database
cur.execute("INSERT INTO Student (name, Age, college) VALUES ('"+name+"','"+Age+"','"+college+"')")

module.msg()

# Fetch all data from DB
for i in cur.execute("SELECT * FROM Student"):
    print(i)
#Commit(save) and close connection  anf close file
con.commit()
con.close()
f.close()
