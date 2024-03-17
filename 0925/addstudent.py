import sqlite3 as lite

con = lite.connect('mydb.db')

with con:
    cur=con.cursor()
    cur.execute("Insert into STUDENT Values('D01', 'THOMAS', 'TUCKER', 3, 'male')")
    cur.execute("Insert into STUDENT Values('D02', 'KAYLEE', 'SIMPSON', 3, 'female')")
    cur.execute("Insert into STUDENT Values('D03', 'LEVI', 'BROOKS', 1, 'male')")
    con.commit()
    
con.close()