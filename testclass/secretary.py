import time

class Secretary:
    def __init__(self):
        self.appointment = {}

    def request_appointment(self, when, who):
        if when in self.appointment:
            return False
        else:
            self.appointment[when] = who
            return True

    def get_schedule(self):
        return str(self.appointment)

        