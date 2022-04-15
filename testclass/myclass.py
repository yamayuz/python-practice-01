
class MyClass:
    a = 'A'

    def __init__(self):
        self.b = 'B'

    def set_ab(self, a, b):
        MyClass.a = a
        self.b = b

    def print_ab(self):
        print(MyClass.a)
        print(self.b)