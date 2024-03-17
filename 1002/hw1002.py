import wx
import sqlite3

conn = sqlite3.connect('1002/dbtest.db')
with conn:
    cur = conn.cursor()

    app = wx.App()
    frame = wx.Frame(None, title="10/02 HW", size=(600, 400))

    nb = wx.Notebook(frame)


    panel1 = wx.Panel(nb)
    panel4 = wx.Panel(nb)
    # 創建SID、Fname、Lname的文本輸入框
    sid_label = wx.StaticText(panel1, label="SID:")
    sid_text = wx.TextCtrl(panel1)

    fname_label = wx.StaticText(panel1, label="Fname:")
    fname_text = wx.TextCtrl(panel1)

    lname_label = wx.StaticText(panel1, label="Lname:")
    lname_text = wx.TextCtrl(panel1)

    # 創建Grade的下拉選單
    grade_label = wx.StaticText(panel1, label="Grade:")
    grade_choices = ["1", "2", "3"]
    grade_combo = wx.ComboBox(panel1, choices=grade_choices, style=wx.CB_DROPDOWN)

    # 創建Sex的選擇按鈕
    sex_label = wx.StaticText(panel1, label="Sex:")
    sex_choices = ["男", "女"]
    sex_radio = wx.RadioBox(panel1, choices=sex_choices, style=wx.RA_HORIZONTAL)

    cur.execute(f'select SID from STUDENT')
    l = cur.fetchall()
    l = [a[0] for a in l]
    student_combo = wx.ComboBox(panel4, choices=l, style=wx.CB_DROPDOWN)


    def on_insert(event):
        # 在這裡添加處理Insert按鈕的代碼
        sid = sid_text.GetValue()
        fname = fname_text.GetValue()
        lname = lname_text.GetValue()
        grade = grade_combo.GetValue()
        sex = sex_choices[sex_radio.GetSelection()]
        student_combo.Append(sid)
        cur.execute(f'insert into STUDENT values(\'{sid}\', \'{fname}\', \'{lname}\', {grade}, \'{sex}\')')
        conn.commit()
    # 創建Insert按鈕
    insert_button = wx.Button(panel1, label="Insert")
    insert_button.Bind(wx.EVT_BUTTON, on_insert)
    # 使用Sizer來安排控件的位置
    sizer = wx.GridSizer(0, 2, 0, 0)
    sizer.Add(sid_label, 0, wx.ALL, 5)
    sizer.Add(sid_text, 0, wx.EXPAND | wx.ALL, 5)
    sizer.Add(fname_label, 0, wx.ALL, 5)
    sizer.Add(fname_text, 0, wx.EXPAND | wx.ALL, 5)
    sizer.Add(lname_label, 0, wx.ALL, 5)
    sizer.Add(lname_text, 0, wx.EXPAND | wx.ALL, 5)
    sizer.Add(grade_label, 0, wx.ALL, 5)
    sizer.Add(grade_combo, 0, wx.EXPAND | wx.ALL, 5)
    sizer.Add(sex_label, 0, wx.ALL, 5)
    sizer.Add(sex_radio, 0, wx.EXPAND | wx.ALL, 5)
    sizer.Add(insert_button, 0, wx.ALL, 5)

    panel1.SetSizer(sizer)


    panel2 = wx.Panel(nb)

    sizer2 = wx.BoxSizer(wx.VERTICAL)

    grade_combo2 = wx.ComboBox(panel2, choices=["1", "2", "3"], style=wx.CB_DROPDOWN)  

    # 创建按钮（Button）
    find_button = wx.Button(panel2, label="Find")
    result_label = wx.StaticText(panel2, label="")

    sizer2.Add(grade_combo2, 0, wx.ALL | wx.EXPAND, 10)
    sizer2.Add(find_button, 0, wx.ALL | wx.CENTER, 10)
    sizer2.Add(result_label, 0, wx.ALL | wx.EXPAND, 10)

    def on_find(event):
        # 在這裡添加處理Insert按鈕的代碼
        grade = grade_combo2.GetValue()
        result_label.SetLabel("")
        cur.execute(f'select * from STUDENT where grade={grade}')
        rows = cur.fetchall()
        for row in rows:
            # s = ''
            # for e in row:
            #     s += e + ' '
            result_label.SetLabel(result_label.Label + "\n" + str(row))
            
        
    find_button.Bind(wx.EVT_BUTTON, on_find)

    # 设置Sizer
    panel2.SetSizer(sizer2)


    panel3 = wx.Panel(nb)

    course_combo = wx.ComboBox(panel3, choices=["C01", "C02"], style=wx.CB_DROPDOWN)

    # 创建静态文本
    text_static = wx.StaticText(panel3, label="")

    # 创建按钮
    cmd_button = wx.Button(panel3, label="count")
    def on_count(event):
        # 在這裡添加處理Insert按鈕的代碼
        course = course_combo.GetValue()
        cur.execute(f'select avg(Score), max(Score), min(Score) from ENROLLMENT where CID = \'{course}\'')
        l = cur.fetchall()
        l = l[0]
        avg_score = l[0]
        max_score = l[1]
        min_score = l[2]
        s = f'Avg Score: {avg_score}\n'
        cur.execute(f'select SID from ENROLLMENT where Score={max_score}')
        sid = cur.fetchone()
        cur.execute(f'select Fname, Lname from STUDENT where SID=\'{sid[0]}\'')
        l = cur.fetchall()
        l = l[0]
        s += f'Max: {l[0]} {l[1]} {max_score}\n'

        cur.execute(f'select SID from ENROLLMENT where Score={min_score}')
        sid = cur.fetchone()
        cur.execute(f'select Fname, Lname from STUDENT where SID=\'{sid[0]}\'')
        l = cur.fetchall()
        l = l[0]
        s += f'Min: {l[0]} {l[1]} {min_score}'

        text_static.SetLabel(s)
        # 在這裡執行插入數據的操作，比如保存到數據庫或顯示消息對話框
    cmd_button.Bind(wx.EVT_BUTTON, on_count)

    # 创建Sizer来布局控件
    sizer3 = wx.BoxSizer(wx.VERTICAL)
    sizer3.Add(course_combo, 0, wx.ALL | wx.EXPAND, 5)
    sizer3.Add(cmd_button, 0, wx.ALL | wx.EXPAND, 5)
    sizer3.Add(text_static, 0, wx.ALL | wx.EXPAND, 5)

    panel3.SetSizer(sizer3)




    text_static2 = wx.StaticText(panel4, label="search with SID and CID")
    search_button = wx.Button(panel4, label="search")

    course_combo2 = wx.ComboBox(panel4, choices=["C01", "C02"], style=wx.CB_DROPDOWN)
    text_static3 = wx.StaticText(panel4, label="Score:")
    text_static4 = wx.StaticText(panel4, label="")
    score_text = wx.TextCtrl(panel4)
    update_button = wx.Button(panel4, label="update")

    def on_search(event):
        # 在這裡添加處理Insert按鈕的代碼
        course = course_combo2.GetValue()
        student = student_combo.GetValue()
        cur.execute(f'select Score from ENROLLMENT where SID=\'{student}\' and CID=\'{course}\'')
        text_static4.SetLabel(f"{cur.fetchone()[0]}")
        
        # 在這裡執行插入數據的操作，比如保存到數據庫或顯示消息對話框
    search_button.Bind(wx.EVT_BUTTON, on_search)

    def on_update(event):
        # 在這裡添加處理Insert按鈕的代碼
        score = score_text.Value
        course = course_combo2.GetValue()
        student = student_combo.GetValue()
        cur.execute(f'update ENROLLMENT set Score={score} where SID=\'{student}\' and CID=\'{course}\'')
        text_static4.SetLabel(f"{score}")
        conn.commit()
        # 在這裡執行插入數據的操作，比如保存到數據庫或顯示消息對話框
    update_button.Bind(wx.EVT_BUTTON, on_update)

    sizer4 = wx.BoxSizer(wx.VERTICAL)
    sizer4.Add(text_static2, 0, wx.ALL | wx.EXPAND, 5)
    sizer4.Add(search_button, 0, wx.ALL | wx.EXPAND, 5)
    sizer4.Add(student_combo, 0, wx.ALL | wx.EXPAND, 5)
    sizer4.Add(course_combo2, 0, wx.ALL | wx.EXPAND, 5)
    sizer4.Add(text_static3, 0, wx.ALL | wx.EXPAND, 5)
    sizer4.Add(text_static4, 0, wx.ALL | wx.EXPAND, 5)
    sizer4.Add(score_text, 0, wx.ALL | wx.EXPAND, 5)
    sizer4.Add(update_button, 0, wx.ALL | wx.EXPAND, 5)

    panel4.SetSizer(sizer4)

    nb.AddPage(panel1, "Insert")
    nb.AddPage(panel2, "Show")
    nb.AddPage(panel3, "Avg")
    nb.AddPage(panel4, "Update")

    sizerf = wx.BoxSizer(wx.VERTICAL)
    sizerf.Add(nb, 1, wx.EXPAND)
    frame.SetSizer(sizerf)


    frame.Show()
    app.MainLoop()
    conn.commit()
    conn.close()