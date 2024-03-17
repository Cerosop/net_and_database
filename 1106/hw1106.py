from flask import Flask, request, render_template
import sqlite3 as lite
app = Flask(__name__)


@app.route('/score', methods=['GET', 'POST'])
def score():
    a = ''
    out = []
    if request.method == 'POST':
        a = request.values['sid']
        con = lite.connect('1106/mydb.db')
        with con:
            cur=con.cursor()
            cur.execute(f"select CID, MidScore, FinalScore, Score from Enrollment where SID = '{a}'")
            con.commit()
            rows = cur.fetchall()
            out.append(a)
            for row in rows:
                out.append(str(row[0]) + ' MidScore:' + str(row[1]) + ' FinalScore:' + str(row[2]) + ' Score:' + str(row[3]))
                
            
        con.close()
        print(out)
        return render_template('score.html', outs=out)
    return render_template('score.html')

if __name__ == '__main__':
    app.debug = True
    app.run()