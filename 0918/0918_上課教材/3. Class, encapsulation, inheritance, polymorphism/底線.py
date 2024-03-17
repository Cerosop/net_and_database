class Test(object):
    def __init__(self):
        self.__a = 'a'
        self._b = 'b'

t= Test()
print(t._b)
print(t._Test__a)    # __a 會被取代成_Test__a
t._b = 'B'
print(t._b)
t._Test__a= "A"
print(t._Test__a)