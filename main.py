from testclass.TestClass import *
from testclass.manager import *
from testclass.client import *
from testclass.calc import *
from testclass.function import *


# def add(a: int, b: int) -> int:
#     return a + b


# def decrease(a: int, b: int) -> int:
#     return a - b


def is_even(x: int) -> int:
    return x % 2 == 0


if __name__ == "__main__":
    filter_object = filter(is_even, range(10))
    print(list(filter_object))

    # calcを使用
    # calc = Calc([("plus", add), ("minus", decrease)])
    # calc.run()
