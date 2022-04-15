from testclass.TestClass import *
from testclass.customer import Customer
from testclass.manager import *
from testclass.client import *
from testclass.calc import *
from testclass.function import *
import random, functools
from testclass.myclass import *
from testclass.customer import *


# def add(a: int, b: int) -> int:
#     return a + b

# def decrease(a: int, b: int) -> int:
#     return a - b


if __name__ == "__main__":
    c = Customer('taro', 25)
    c.print_info()
    print(c)


    # calcを使用
    # calc = Calc([("plus", add), ("minus", decrease)])
    # calc.run()
