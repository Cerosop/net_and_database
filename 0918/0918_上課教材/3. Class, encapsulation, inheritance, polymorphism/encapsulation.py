class Car:
    Name=""
    def __init__(self, CName):
        self.Name=CName
        self.__updateSoftware()    #只能夠在定義CLASS中使用。不可外界(物件)呼叫 

    def __updateSoftware(self):
        print("updating software")

    def drive(self):
        print("driving" + self.Name)
    
Toyota= Car("Toyota")
Toyota.drive()
# Toyota.__updateSoftware()   只能夠在定義CLASS中使用。不可外界(物件)呼叫 
