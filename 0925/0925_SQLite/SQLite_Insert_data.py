import sqlite3 as lite

con = lite.connect('Programmer.db')

with con:
    cur=con.cursor()
    cur.execute("Insert into Programmer Values(1, 'Diana', 'Python')")
    cur.execute("Insert into Programmer Values(2, 'John', 'C')")
    con.commit()
    
con.close()