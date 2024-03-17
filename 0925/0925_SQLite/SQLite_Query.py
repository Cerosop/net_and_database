import sqlite3 

conn=sqlite3.connect ('Programmer.db')
cur=conn.cursor()
cur.execute ("select * from Programmer")

#rows = cur.fetchall()
#for row in rows:
#    print(row)
row=cur.fetchone()
print(row)
row=cur.fetchone()
print(row)

conn.commit()
conn.close()