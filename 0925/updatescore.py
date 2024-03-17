import sqlite3 as lite

con = lite.connect('mydb.db')
cur = con.cursor()
with con:
    cur.execute("update Enrollment set MidScore=50, FinalScore=100, Score=85 where SID='D01' and CID='C01'")
    cur.execute("update Enrollment set MidScore=60, FinalScore=80, Score=54 where SID='D02' and CID='C01'")
    cur.execute("update Enrollment set MidScore=20, FinalScore=75, Score=58.5 where SID='D03' and CID='C02'")
    
con.close()