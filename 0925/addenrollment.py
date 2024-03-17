import sqlite3 as lite

con = lite.connect('mydb.db')

with con:
    cur=con.cursor()
    cur.execute("Insert into Enrollment (SID, CID) Values('D01', 'C01')")
    cur.execute("Insert into Enrollment (SID, CID) Values('D02', 'C01')")
    cur.execute("Insert into Enrollment (SID, CID) Values('D03', 'C02')")
    con.commit()
    
con.close()