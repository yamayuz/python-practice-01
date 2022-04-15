# 特殊メソッドのオーバーライド
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # objectでは、__str__はアドレス番地を出力する
    # インスタンス変数を出力するように、__str__をオーバーライド
    def __str__(self):
        return 'name:{}, age:{}'.format(self.name, self.age)

    def print_info(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

    