
import csv

with open('test.csv', 'w', newline='') as csvfile:   #記得要有newline=''否則不能正確解讀換行
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Profession'])                                #記得要在open指令下執行寫入，否則I/O會不允許
    filewriter.writerow(['Derek', 'Software Developer'])
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])
    
with open('test.csv', 'r', newline='') as csvfile2:
    filereader=csv.reader(csvfile2)
    for row in filereader:
        print(row)

with open('test.csv', 'r', newline='') as csvfile3:
    filereader=csv.reader(csvfile3)
    for row in filereader:
        print(row[0])