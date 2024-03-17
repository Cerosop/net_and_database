import sqlite3 as lite

con = lite.connect('mydb.db')

with con:
    cur=con.cursor()
    cur.execute("Insert into COURSE Values('C01', '計概')")
    cur.execute("Insert into COURSE Values('C02', '網路概論')")
    con.commit()
    
con.close()