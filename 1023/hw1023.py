from pymongo import MongoClient
import pprint
from PIL import Image
import wx
import io
client = MongoClient(host='localhost', port=27017)
db = client.School


class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        self.tmp = {}
        self.isfind = False
        self.client = MongoClient(host="localhost", port=27017)
        self.db = self.client.School
    
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.name = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"enter name", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.name, 0, wx.ALL, 5 )

        self.phone = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"enter phone", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.phone, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
        self.m_button1.Bind(wx.EVT_BUTTON, self.on_insert)

        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        self.m_notebook1.AddPage( self.m_panel1, u"Insert", False )
        self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 4, 3, 0, 0 )

        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"post name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.post_name = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"enter name", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.post_name, 0, wx.ALL, 5 )

        self.check = wx.Button( self.m_panel2, wx.ID_ANY, u"check", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.check, 0, wx.ALL, 5 )
        self.check.Bind(wx.EVT_BUTTON, self.on_find)

        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"image file address:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.file_address = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"enter address", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.file_address, 0, wx.ALL, 5 )

        self.is_found = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.is_found.Wrap( -1 )

        gSizer1.Add( self.is_found, 0, wx.ALL, 5 )

        self.tag_type = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"tag_type", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.tag_type, 0, wx.ALL, 5 )

        self.tag_text = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"tag_text", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.tag_text, 0, wx.ALL, 5 )

        self.add_tag = wx.Button( self.m_panel2, wx.ID_ANY, u"add_tag", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.add_tag, 0, wx.ALL, 5 )
        self.add_tag.Bind(wx.EVT_BUTTON, self.on_addTag)

        self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"tags:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.tags = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.tags.Wrap( -1 )

        gSizer1.Add( self.tags, 0, wx.ALL, 5 )

        self.upload = wx.Button( self.m_panel2, wx.ID_ANY, u"upload", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.upload, 0, wx.ALL, 5 )
        self.upload.Bind(wx.EVT_BUTTON, self.on_upload)

        self.m_panel2.SetSizer( gSizer1 )
        self.m_panel2.Layout()
        gSizer1.Fit( self.m_panel2 )
        self.m_notebook1.AddPage( self.m_panel2, u"Image", False )
        self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.to_search = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"enter name", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.to_search, 0, wx.ALL, 5 )

        self.search = wx.Button( self.m_panel3, wx.ID_ANY, u"search", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.search, 0, wx.ALL, 5 )
        self.search.Bind(wx.EVT_BUTTON, self.on_search)

        self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"tags:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.tags2 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.tags2.Wrap( -1 )

        gSizer3.Add( self.tags2, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( gSizer3 )
        self.m_panel3.Layout()
        gSizer3.Fit( self.m_panel3 )
        self.m_notebook1.AddPage( self.m_panel3, u"Search", True )

        bSizer1.Add( self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass  
    
    def on_insert(self, event): 
        ST1 = { "name": self.name.GetValue(), "phone": self.phone.GetValue()}
        self.db.STUDENT.insert_many([ST1])

    def on_find(self, event): 
        self.isfind = False
        self.is_found.SetLabel("not found")
        self.tmp = {}
        for STs in self.db.IMAGE.find({"name": self.post_name.GetValue()}):
            self.isfind = True
            self.is_found.SetLabel("found")
            
            for key in STs:
                if key != "_id" and key != "name" and key != "image":
                    self.tmp[key] = STs[key]
                    self.tags.LabelText = self.tags.GetValue() + "\n" + key + ": " + STs[key]           
            
    def on_addTag(self, event): 
        self.tmp[self.tag_type.GetValue()] = self.tag_text.GetValue()
        self.tags.LabelText = ""
        for key in self.tmp:
                self.tags.LabelText = self.tags.LabelText + "\n" + key + ": " + self.tmp[key]

    def on_upload(self, event): 
        self.isfind = False
        for STs in self.db.IMAGE.find({"name": self.post_name.GetValue()}):
            self.isfind = True
            
            for key in STs:
                if key != "_id" and key != "name" and key != "image" and key not in self.tmp:
                    self.tmp[key] = STs[key] 
        im = Image.open(self.file_address.GetValue())
        image_bytes = io.BytesIO()
        if self.file_address.GetValue()[-3:] == "png":
            im.save(image_bytes, format='PNG')
        else:
            im.save(image_bytes, format='JPEG')
        ST1 = { "name": self.post_name.GetValue(), "image": image_bytes.getvalue()}
        for key in self.tmp:
            ST1[key] = self.tmp[key]
        if self.isfind == False:
            self.db.IMAGE.insert_one(ST1)
        else:
            for a, b in ST1.items():
                self.db.IMAGE.update_many({ 'name': self.post_name.GetValue() }, { '$set': { a : b } })
        self.tmp = {}
            
    def on_search(self, event):
        name = self.to_search.GetValue()
        tags = ""
        if not db.IMAGE.find_one({'name':name}):
            self.tags2.SetLabel('not found')
        else:
            name = db.IMAGE.find_one({'name':name})
            for tag_type, tag_text in name.items():
                if tag_type == '_id' or  tag_type == 'name':
                    continue
                if tag_type == 'image':
                    pil_img = Image.open(io.BytesIO(tag_text))
                    pil_img.show()
                    continue
                tags += tag_type + ' : ' + tag_text
                if db.STUDENT.find({'name':tag_text}):
                    other_name = db.STUDENT.find_one({'name':tag_text})
                    if other_name:
                        phone = db.STUDENT.find({'name':tag_text})[0]['phone']
                        tags += f' ({phone})'
                tags += '\n'
            self.tags2.SetLabel(tags)
        print(tags)


app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()