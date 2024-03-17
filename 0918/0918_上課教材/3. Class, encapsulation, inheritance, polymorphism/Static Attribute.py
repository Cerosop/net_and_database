class Student:
    Number = 0                      # Number為static 變數
    name=""
    def __init__(self, Sname, Num):
        self.name=Sname             # self.Number為物件屬性     
        self.Number=Num

s1=Student("John", 1)
Student.Number=Student.Number+1 
print(s1.name," ", s1.Number)  
print(Student.Number)  

s2=Student("Mary", 2)
print(s2.name," ", s2.Number)
Student.Number=Student.Number+1
print(Student.Number)  
