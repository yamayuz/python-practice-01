from inheritance_class.class_ab import *
from inheritance_class.class_pc import *
from inheritance_class.register import *


if __name__ == "__main__":
    c = ConsoleRegister('10.0.0.1')
    c.register()

    w = WebRegister('10.0.0.1')
    w.register()
