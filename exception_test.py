from myerror_class.myerror import *


try:
    raise MyError('my error happens')
except MyError as e:
    print(type(e))
    print(e)