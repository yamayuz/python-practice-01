
class ClassA:
    def __init__(self):
        self.var_a = 'class a'

    def print_a(self):
        print('this method is defined in ' + self.var_a)


class ClassB(ClassA):
    def __init__(self):
        self.var_b = 'class b'
        super().__init__()

    def print_b(self):
        print('this method is defined in ' + self.var_b)
        print('parent of ' + self.var_b + ' is ' + self.var_a)