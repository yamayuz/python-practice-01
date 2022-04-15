
try:
    # f = open('helloworld.txt', 'r')
    5 / 0

except OSError:
    print('os error')

except Exception:
    print('exception')