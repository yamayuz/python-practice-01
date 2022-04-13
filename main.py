from testclass.TestClass import *
from testclass.manager import *
from testclass.client import *
from testclass.calc import *
from testclass.function import *
import random, functools


# def add(a: int, b: int) -> int:
#     return a + b

# def decrease(a: int, b: int) -> int:
#     return a - b


if __name__ == "__main__":
    list_ = [x*2 for x in range(10) if x % 2 == 0]
    print(list_)

    # calcを使用
    # calc = Calc([("plus", add), ("minus", decrease)])
    # calc.run()
