from myerror_class.myerror import *
import traceback

# ---------------------------------------
# 自作例外クラスお試し
# ---------------------------------------
# try:
#     raise MyError('my error happens')
# except MyError as e:
#     print(type(e))
#     print(e)


# ---------------------------------------
# tracebackお試し
# ---------------------------------------
# print(1)
# try:
#     print(2)
#     5 / 0
#     print(3)
# except Exception:
#     print(4)
#     text = traceback.format_exc()
#     print(text)
#     f = open('error.log', 'a')
#     traceback.print_exc(file=f)

# print(5)


# ---------------------------------------
# 例外の返却
# ---------------------------------------
def fun1():
    try:
        raise Exception('error in fun1()')
    except:
        print("1: fun1 can't handle this error")
        raise

def fun2():
    try:
        print('2: call fun1')
        fun1()
        print('3: done')
    except Exception as e:
        print('4: catch error which happens in fun1()')
        print(e)

fun2()