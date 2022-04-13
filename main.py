from testclass.TestClass import *
from testclass.manager import *
from testclass.client import *
from testclass.calc import *


def add(a, b):
    return a + b


def decrease(a, b):
    return a - b


if __name__ == "__main__":
    calc = Calc([("plus", add), ("minus", decrease)])
    calc.run()
