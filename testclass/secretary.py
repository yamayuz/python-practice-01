import time

class Secretary:
    def __init__(self):
        self.logfile = '_log.txt'

    def write_log(self, text):
        log = "{}: {}\n".format(time.ctime(), text)
        f = open(self.logfile, 'a')
        f.write(log)
        f.close()

    def get_log(self):
        f = open(self.logfile, 'r')
        log = f.read()
        f.close()
        return log