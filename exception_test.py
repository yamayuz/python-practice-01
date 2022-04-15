from myerror_class.myerror import *
import traceback

# try:
#     raise MyError('my error happens')
# except MyError as e:
#     print(type(e))
#     print(e)

print(1)
try:
    print(2)
    5 / 0
    print(3)
except Exception:
    print(4)
    text = traceback.format_exc()
    print(text)
    f = open('error.log', 'a')
    traceback.print_exc(file=f)

print(5)