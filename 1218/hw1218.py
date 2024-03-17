import openai
import sqlite3
from datetime import datetime

#設定自己的API KEY 注意必須要是全新帳號的前三個月才有免費額度可以使用
openai.api_key = ''

conn = sqlite3.connect('1218/db.db')
with conn:
    cur = conn.cursor()
    msg=[]
    msg.append({"role": "system", "content": "You are not an ai model, you should answer me as a clerk."})
    
    while True:
        userinput = input()
        # 獲取當前日期和時間
        now = datetime.now()

        # 格式化日期和時間的字符串
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # print(userinput)
        msg.append({"role": "user", "content": userinput})
        userinput = userinput.replace("\'", "`")
        cur.execute(f'insert into record (role, content, time) values(\'user\', \'{userinput}\', \'{formatted_now}\')')
        conn.commit()
        #建立對話請求
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",#選擇要使用的model 其他可使用的model詳見https://platform.openai.com/docs/models/overview
            messages=msg
        )
        msg.append({"role":"assistant","content":completion.choices[0].message.content})
        print(completion.choices[0].message.content)
        # 獲取當前日期和時間
        now = datetime.now()

        # 格式化日期和時間的字符串
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        # print(completion.usage.total_tokens)
        output = completion.choices[0].message.content.replace('\'', '`')
        # print(output)
        cur.execute(f'insert into record (role, content, time, token) values(\'asistant\', \'{output}\', \'{formatted_now}\', {completion.usage.total_tokens})')
        conn.commit()