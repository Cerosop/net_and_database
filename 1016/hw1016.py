import wx
import wx.xrc
import MySQLdb
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = wx.App()

db=MySQLdb.connect(host="localhost", user="newuser", password="f122673674", db="test")
print ("connected")
cur = db.cursor()

cur.execute("SHOW TRIGGERS LIKE 'ENROLLMENT'")
b = False
for emp in cur.fetchall():
    if emp[0] == 'mytrigger':
        b = True
        break
if not b:
    cur.execute(f"CREATE TRIGGER mytrigger AFTER INSERT ON ENROLLMENT FOR EACH ROW BEGIN IF NEW.SCORE < 60 THEN INSERT INTO REMINDERS VALUES(NEW.SID, NEW.CID); END IF; END")

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"SID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.sid = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.sid, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"CID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.cid = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cid, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MidScore", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.midscore = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.midscore, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"FinalScore", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.finalscore = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.finalscore, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Score", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.score = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.score, 0, wx.ALL | wx.EXPAND, 5 )

        self.insert = wx.Button( self.m_panel1, wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.insert, 0, wx.ALL, 5 )
        self.insert.Bind(wx.EVT_BUTTON, self.on_insert)

        self.m_panel1.SetSizer( gSizer1 )
        self.m_panel1.Layout()
        gSizer1.Fit( self.m_panel1 )
        self.m_notebook1.AddPage( self.m_panel1, u"insert score", True )
        self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"students who failed in exam", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )



        self.m_button5 = wx.Button( self.m_panel2, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button5.Bind(wx.EVT_BUTTON, self.on_show)
        gSizer3.Add( self.m_button5, 0, wx.ALL, 5 )


        self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        gSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( gSizer3 )
        self.m_panel2.Layout()
        gSizer3.Fit( self.m_panel2 )
        self.m_notebook1.AddPage( self.m_panel2, u"failed warning", False )

        bSizer1.Add( self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5 )

        self.notify = wx.Button( self.m_panel2, wx.ID_ANY, u"Notify parents", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.notify.Bind(wx.EVT_BUTTON, self.on_notify)
        gSizer3.Add( self.notify, 0, wx.ALL, 5 )
        
        self.m_staticText12 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        gSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )
    
    def on_insert(self, event):
        cur.execute(f"insert into enrollment values(\'{self.sid.GetValue()}\', \'{self.cid.GetValue()}\', \'{self.midscore.GetValue()}\', \'{self.finalscore.GetValue()}\', \'{self.score.GetValue()}\')")
        db.commit()
        return
    
    def on_show(self, event):
        cur.execute("Select * from reminders")
        for emp in cur.fetchall():
            sid = emp[0]
            cid = emp[1]
            self.m_staticText11.SetLabel(self.m_staticText11.Label + "\n" + "Student " + sid + " fail in " + cid)
    
    def on_notify(self, event):
        cur.execute("Select * from reminders")
        for emp in cur.fetchall():
            sid = emp[0]
            cid = emp[1]
            cur2=db.cursor()
            cur2.execute(f"Select Fname, Lname, Pemail from student where SID = \'{sid}\'")
            for emp2 in cur2.fetchall():
                Fname = emp2[0]
                Lname = emp2[1]
                email = emp2[2]
          
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = "jmhsu920816@gmail.com"  
                smtp_password = "bfgv dadp qoej bnod" 

                msg = MIMEMultipart()
                msg['From'] = smtp_username
                msg['To'] = email  
                msg['Subject'] = "Notify parents"

               
                message = "Your child " + sid + " " +Fname + " " + Lname + " failed in course " + cid + "."
                msg.attach(MIMEText(message, 'plain'))

                
                try:
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls() 
                    server.login(smtp_username, smtp_password)
                    server.sendmail(smtp_username, msg['To'], msg.as_string())
                    server.quit()
                    self.m_staticText12.SetLabel(self.m_staticText12.Label + "\n" + sid + ": successfully")
    
                    print("email sent!")
                except Exception as e:
                    self.m_staticText12.SetLabel(self.m_staticText12.Label + "\n" + sid + ": failed")
                    print("email failed:", str(e))
                

    def __del__( self ):
        pass

frame = MyFrame2(None)
frame.Show()
app.MainLoop()