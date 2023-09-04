from tkinter import *
from threading import Thread
from time import sleep
from ping3 import ping

"""
    root = tk.Tk()
    for r in range(3):
        for c in range(4):
            tk.Label(root, text='R%s/C%s' % (r, c),
                     borderwidth=1).grid(row=r, column=c)
    root.mainloop()
"""


def background_task():

    while True:
        if ping("192.168.100.2") != False:
            # report the change
            btn.config(fg="green")
            print("Comp is running")
        else:
            btn.config(fg="red")
        sleep(1)

daemon = Thread(target=background_task, daemon=True)
daemon.start()



root = Tk()



button_frame = Frame(root)


list = ["pc1", "pc2", "pc3"]
btn1 = ""
btn2 = ""
btn3 = ""

buttons = [btn1, btn2, btn3]
for r in range(len(list)):
    for c in range(2):
        btn = Button(button_frame, text="START 0%s" % (r + 1), borderwidth=1)
        btn.grid(row=r, column=0)


"""
for r in range(len(list)):
    for c in range(2):
        a += [(r, c)]
        bt = Button(button_frame, text="STOP 0%s" % (r + 1),
               borderwidth=1).grid(row=r, column=1)


btn1 = Button(button_frame, text="1")
btn1.grid(row=0, column=0, sticky=W + E)

btn2 = Button(button_frame, text="2")
btn2.grid(row=1, column=0, sticky=N+S)
"""



button_frame.pack()

root.mainloop()