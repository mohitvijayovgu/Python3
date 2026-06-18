class MyClass:
    # class variables
    var1 = "Ansh"
    var2 = "Lamba"

    # instance variables
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1 = dyn1
        self.dyn2 = dyn2
        self.dyn3 = dyn3


    def func1(self):
        print(f"Hello World, {self.dyn1}")

    def func2(self):
        print(f"Hello Globe, {self.dyn2}")

    def func3(self):
        print(f"Hello Universe, {self.dyn3}")

# create python object
obj = MyClass("abc","def","ghi")
obj.func1()

# another way of writing
MyClass.func1(obj)

obj_new = MyClass("xyz","pqr","stu")
obj_new.var2 = "changed"
print(obj_new.var2)