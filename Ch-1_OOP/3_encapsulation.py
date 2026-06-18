class MyClass:
    # class variables
    var1 = "Ansh"
    var2 = "Lamba"

    # instance variables
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1 = dyn1 # public variable
        self.__dyn2 = dyn2 # private variable
        self._dyn3 = dyn3 # protected variable


    def func1(self):
        print(f"Hello World, {self.dyn1}")

    def func2(self):
        print(f"Hello Globe, {self.__dyn2}")

    def func3(self):
        print(f"Hello Universe, {self.dyn3}")

# create python object
obj = MyClass("abc","def","ghi")
obj.dyn1 = "pqr"
print(obj.dyn1)
obj.func1()

obj.dyn2 = "stu"
print(obj.dyn2)

obj.func2()


print(obj._dyn3)
print(obj.__dyn2)


