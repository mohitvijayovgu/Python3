class MyClass:

    my_var = 100

    #dunder method or special methods

    def __init__(self):
        print("This is constructor method")

    # Dunder method for string
    def __str__(self):
       return "This is string method"

    @classmethod
    def _change_value(cls, new_value):
      cls.my_var = new_value

    @staticmethod
    def dummy():
       print("This is a dummy method")

# obj = MyClass()
# print(obj.my_var)
# obj._change_value(200)
# print(obj.my_var)  
# obj2 = MyClass()
# print(obj2.my_var)
# obj3 = MyClass()
# print(obj3.dummy())
obj4 = MyClass()
print(obj4)