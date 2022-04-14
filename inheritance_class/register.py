
class Register:
    def __init__(self, dbip):
        self.dbip = dbip

    def register(self, text):
        print('write "{}" to DB Server at {}'.format(text, self.dbip))


class ConsoleRegister(Register):
    def __init__(self, dbip):
        super().__init__(dbip)

    def register(self):
        text = 'input from Console'
        super().register(text)


class WebRegister(Register):
    def __init__(self, dbip):
        super().__init__(dbip)

    def register(self):
        text = 'input from REST'
        super().register(text)
