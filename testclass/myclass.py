
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


# クラスメソッドの例
class MyClass2:
    a = 'A'

    @classmethod
    def print_hello(cls):
        print(cls.a)
        print(type(cls))


# スタティックメソッドの例
class MyClass3:
    a = 'A'

    @staticmethod
    def print_a():
        print(MyClass3.a)

