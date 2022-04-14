from counter_class.counter1 import *
from counter_class.counter2 import *

if __name__ == "__main__":
    # c = Counter1(0)

    f = tk.Frame()
    c1 = Counter2(value=0, master=f)
    c2 = Counter2(value=5, master=f)
    c1.pack()
    c2.pack()
    f.pack()
    f.mainloop()