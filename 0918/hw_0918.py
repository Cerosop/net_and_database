import csv
name = input('name: ')
score1 = input('score1: ')
score2 = input('score2: ')
print('')

with open('score.csv', 'a', newline='') as csvfile:   #記得要有newline=''否則不能正確解讀換行
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([name, score1, score2, ''])
    
print('新增一筆學生成績資料')
with open('score.csv', 'r', newline='') as csvfile:
    filereader=csv.reader(csvfile)
    rows = list(filereader)
    for row in rows:
        print(row)
    print('')
    
 
with open('score.csv', 'r', newline='') as csvfile:
    filereader=csv.reader(csvfile)
    rows = list(filereader)
    for row in rows:
        if row[0] == '李小明':
            row[1] = 60
            
    with open('score.csv', mode='w', newline='') as csvfile2:
        filewriter = csv.writer(csvfile2, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerows(rows)
        
print('修改「李小明」的期中成績為60分')
with open('score.csv', 'r', newline='') as csvfile:
    filereader=csv.reader(csvfile)
    rows = list(filereader)
    for row in rows:
        print(row)
    print('')
        

with open('score.csv', 'r', newline='') as csvfile:
    filereader=csv.reader(csvfile)
    rows = list(filereader)
    for i, row in enumerate(rows):
        if i > 0:
            row[3] = str(int(row[1]) * 0.3 + int(row[2]) * 0.7)
            
    with open('score.csv', mode='w', newline='') as csvfile2:
        filewriter = csv.writer(csvfile2, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerows(rows)

print('計算出學期成績')       
with open('score.csv', 'r', newline='') as csvfile:
    filereader=csv.reader(csvfile)
    rows = list(filereader)
    for row in rows:
        print(row)
    print('')