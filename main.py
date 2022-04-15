from testclass.TestClass import *
from testclass.manager import *
from testclass.client import *
from testclass.calc import *
from testclass.function import *
import random, functools
from testclass.myclass import *


# def add(a: int, b: int) -> int:
#     return a + b

# def decrease(a: int, b: int) -> int:
#     return a - b


if __name__ == "__main__":
    taro_calc = Calc2(0.95)
    print(taro_calc.get_price(10000))


    # calcを使用
    # calc = Calc([("plus", add), ("minus", decrease)])
    # calc.run()
