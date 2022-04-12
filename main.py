from testclass.TestClass import *
from testclass.manager import *
from testclass.client import *


def fun1(fun, test):
    fun(test)


def fun2(text):
    print('fun2:' + text)


if __name__ == "__main__":
    fun1(fun2, 'hello')
