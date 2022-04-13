# クロージャ
def adder(x: int):
    def fun(y: int) -> int:
        return x + y

    return fun


# ラムダ関数
my_print = lambda x : print('my_print : {}'.format(x))