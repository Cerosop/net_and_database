import json
from flask import Flask, jsonify, request, render_template, redirect
import sqlite3 as lite
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
app = Flask(__name__)


@app.route('/')
def redir():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    con = lite.connect('期中/mydb.db')
    acc = ''
    if request.method == 'POST':
        acc = request.values['acc']
        pas = request.values['pas']
        
        with con:
            cur=con.cursor()
            cur.execute(f"select pas from User where acc = '{acc}'")
            con.commit()
            rows = cur.fetchall()
            if not rows:
                data = {'res': '0'}
                return jsonify(data)
            for row in rows:
                if pas == row[0]:
                    data = {'res': '1', 'acc': acc}
                    return jsonify(data)
                else:
                    data = {'res': '-1'}
                    return jsonify(data)
    else:
        return render_template('test2.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    con = lite.connect('期中/mydb.db')
    acc = ''
    if request.method == 'POST':
        acc = request.values['acc2']
        pas = request.values['pas2']
        mai = request.values['mai']
        gen = request.values.get('gender')
        col = request.values['col']
        if acc == "" or pas == "" or gen == "" or mai == "":
            data = {'res': '-1', 'acc': '-1'}
            return jsonify(data)
        
        with con:
            cur=con.cursor()
            cur.execute(f"select * from User where acc = '{acc}'")
            con.commit()
            rows = cur.fetchall()
            if not rows:
                cur.execute(f"Insert into User Values('{acc}', '{pas}', '{mai}', '{gen}', '{col}', 'F')")
                con.commit()
                
                data = {'res': '1', 'acc': acc}
                return jsonify(data)
            else:
                data = {'res': '0', 'acc': '0'}
                return jsonify(data)
                    
        
    return render_template('test3.html')

@app.route('/home/', methods=['GET', 'POST'])
@app.route('/home/<acc>', methods=['GET', 'POST'])
def home(acc = None):
    return render_template('test4.html')

@app.route('/home/members/', methods=['GET', 'POST'])
@app.route('/home/members/<acc>', methods=['GET', 'POST'])
def members(acc = None):
    con = lite.connect('期中/mydb.db')
    
    with con:
        cur=con.cursor()
        cur.execute("select * from User")
        con.commit()
        rows = cur.fetchall()
        res = []
        if rows:
            for row in rows:
                m = {}
                m['acc'] = row[0]
                m['mai'] = row[2]
                m['gen'] = row[3]
                m['col'] = row[4]
                res.append(m)
    
    return render_template('test4_1.html', outs = res)
                
   
@app.route('/home/update/', methods=['GET', 'POST'])
@app.route('/home/update/<acc>', methods=['GET', 'POST'])
def update(acc = None):
    con = lite.connect('期中/mydb.db')
    if request.method == 'POST':
        aci = request.values['acc3']
        pas = request.values['pas3']
        mai = request.values['mai3']
        gen = request.values.get('gender3')
        col = request.values['col3']
        
        
        with con:
            cur=con.cursor()
            if aci == "" or pas == "" or gen == "" or mai == "":
                data = {'res': '-1'} #no input
                return jsonify(data)
            elif aci != acc:
                cur.execute(f"select * from User where acc = '{aci}'")
                con.commit()
                rows = cur.fetchall()
                if rows:
                    data = {'res': '0'} #aci exist
                    return jsonify(data)
            
            cur.execute(f"update User set acc='{aci}', pas='{pas}', email='{mai}', gender='{gen}', color='{col}' where acc = '{acc}'")
            con.commit()
            cur.execute(f"update File set acc='{aci}' where acc = '{acc}'")
            con.commit()
            data = {'res': '1'}
            return jsonify(data)
        
    
    
    with con:
        cur=con.cursor()
        cur.execute(f"select * from User where acc = '{acc}'")
        con.commit()
        rows = cur.fetchall()
        outs = []
        if not rows: 
            outs.append('0')
        else:
            outs.append('1')
            for row in rows[0]:
                outs.append(row)
    return render_template('test4_2.html', res=outs, acc2=acc)

@app.route('/home/sub/', methods=['GET', 'POST'])
@app.route('/home/sub/<acc>', methods=['GET', 'POST'])
def sub(acc = None):
    con = lite.connect('期中/mydb.db')
    if request.method == 'POST':
        
        with con:
            cur=con.cursor()
            cur.execute(f"select * from User where acc = '{acc}'")
            con.commit()
            rows = cur.fetchall()
            outs = []
            if not rows: 
                data = {'res': '0'}
                return jsonify(data)
            else:
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = "jmhsu920816@gmail.com"  
                smtp_password = "bfgv dadp qoej bnod" 

                msg = MIMEMultipart()
                msg['From'] = smtp_username
                msg['To'] = rows[0][2] 
                msg['Subject'] = "Notify subscription"
                if rows[0][5] == 'T':
                    cur=con.cursor()
                    cur.execute(f"update User set sub='F' where acc = '{acc}'")
                    con.commit()
                    
                    message = f"{rows[0][0]} has canceled subsription of our web."
                    msg.attach(MIMEText(message, 'plain'))

                    try:
                        server = smtplib.SMTP(smtp_server, smtp_port)
                        server.starttls() 
                        server.login(smtp_username, smtp_password)
                        server.sendmail(smtp_username, msg['To'], msg.as_string())
                        server.quit()
                        print("email sent!")
                    except Exception as e:
                        print("email failed:", str(e))
                        
                    data = {'res': '1'}
                    return jsonify(data)
                else:
                    cur=con.cursor()
                    cur.execute(f"update User set sub='T' where acc = '{acc}'")
                    con.commit()
                    
                    message = f"{rows[0][0]} has subsribed our web."
                    msg.attach(MIMEText(message, 'plain'))

                    try:
                        server = smtplib.SMTP(smtp_server, smtp_port)
                        server.starttls() 
                        server.login(smtp_username, smtp_password)
                        server.sendmail(smtp_username, msg['To'], msg.as_string())
                        server.quit()
                        print("email sent!")
                    except Exception as e:
                        print("email failed:", str(e))
                    
                    data = {'res': '2'}
                    return jsonify(data)
            
    with con:
        cur=con.cursor()
        cur.execute(f"select * from User where acc = '{acc}'")
        con.commit()
        rows = cur.fetchall()
        outs = []
        if not rows: 
            outs.append('0')
        else:
            outs.append('1')
            print(type(rows[0][5]))
            outs.append(rows[0][5])
    return render_template('test4_3.html', res=outs, acc2=acc)


@app.route('/home/file/', methods=['GET', 'POST'])
@app.route('/home/file/<acc>', methods=['GET', 'POST'])
def file(acc = None):
    con = lite.connect('期中/mydb.db')
    if request.method == 'POST':
        todo = ''
        data = ''
        a = request.get_json()
        todo = a['todo']
        data = a['data'] 
            
        if todo == 'upload':
            with con:
                cur=con.cursor()
                cur.execute(f"Insert into File (name, size, time, file, acc) Values('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{acc}')")
                con.commit()
                data = {'id': cur.lastrowid}
                return jsonify(data)
        elif todo == 'download':
            with con:
                cur=con.cursor()
                cur.execute(f"select file, name from File where id = {data}")
                con.commit()
                rows = cur.fetchall()
                data = {'file': rows[0][0], 'name': rows[0][1]}
                return jsonify(data)
        elif todo == 'delete':
            with con:
                cur=con.cursor()
                cur.execute(f"delete from File where id = {data}")
                con.commit()
                data = {'id': data}
                return jsonify(data)
            
    with con:
        cur=con.cursor()
        cur.execute(f"select * from User where acc = '{acc}'")
        con.commit()
        rows = cur.fetchall()
        outs = []
        if not rows: 
            outs.append('0')
        else:
            outs.append('1')
            cur.execute(f"select * from File where acc = '{acc}'")
            con.commit()
            rows = cur.fetchall()
            out = []
            for row in rows:
                out.append(row)
            outs.append(out)
    return render_template('test4_4.html', res=outs, acc2=acc)

if __name__ == '__main__':
    app.debug = True
    app.run()