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
    mycls_a = MyClass()
    mycls_b = MyClass()

    mycls_a.print_ab()
    mycls_b.print_ab()

    mycls_a.set_ab('AA', 'BB')

    mycls_a.print_ab()
    mycls_b.print_ab()


    # calcを使用
    # calc = Calc([("plus", add), ("minus", decrease)])
    # calc.run()
