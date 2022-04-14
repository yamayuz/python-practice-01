import tkinter as tk

frame1 = tk.Frame()

# Child1
frame2 = tk.Frame(frame1)
font = ('Helevetica', 32, 'bold')
label1 = tk.Label(frame2, text='Hello Tk', font=font, bg='red')
label2 = tk.Label(frame2, text='Hello Python', font=font, bg='blue')
label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
frame2.pack()

# Child2
label3 = tk.Label(frame1, text='Hello World', font=font, bg='green')
label3.pack(fill=tk.X)

frame1.pack()
frame1.mainloop()