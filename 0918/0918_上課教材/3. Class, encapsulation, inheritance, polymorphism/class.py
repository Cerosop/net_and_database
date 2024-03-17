class user:
    name =""
    def __init__(self, name):
        self.name=name
    def PrintName(self):
        print("Name = " + self.name)

John = user("John")
John.PrintName()

