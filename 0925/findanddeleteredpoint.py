import sqlite3 as lite

con = lite.connect('mydb.db')

with con:
    cur=con.cursor()
    cur.execute("select SID, CID from Enrollment where Score < 60 and CID = 'C01'")
    con.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
        print("delete from Enrollment where SID = '{}' AND CID = 'C01'".format(row[0]))
        
    
con.close()