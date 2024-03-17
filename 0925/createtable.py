import sqlite3 as lite

con = lite.connect('mydb.db')
cur = con.cursor()
with con:
    cur.execute("create table STUDENT (SID primary key, Fname, Lname, Grade, Sex)")
    cur.execute("create table COURSE (CID primary key, Fname)")
    cur.execute("create table Enrollment (SID, CID, MidScore default 0, FinalScore default 0, Score default 0, foreign key(SID) references STUDENT(SID), primary key(SID, CID))")
    
con.close()