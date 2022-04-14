
class Parent:
    def __init__(self):
        print('Parent __init__()')

    def fun1(self):
        print('Parent fun1()')

    def fun2(self):
        print('Parent fun2()')


class Child(Parent):
    def __init__(self):
        print('Child __init__()')

    def fun1(self):
        print('Child fun1()')
    