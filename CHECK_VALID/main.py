from tkinter import *
from threading import Thread
from ping3 import ping
import time

"""" 
command = ["python3", "sub.py"]
# p1 = subprocess.run(command, capture_output=True, text=True)
p1 = subprocess.run(command, stdout=subprocess.PIPE, text=True)


print(p1.stdout)
print("yo")
"""


def background_task():
    while True:
        time.sleep(2)
        if ping("192.168.100.2") != False:
            btn.config(fg="green")

        else:
            btn.config(fg="red")

        print(ping("192.168.100.2"))

daemon = Thread(target=background_task, daemon=True)
daemon.start()


root = Tk()


root.geometry("200x200")

for r in range(3):
    for c in range(2):
        btn = Button(root,
                     text="OFF",
                     )
        btn.pack()



root.mainloop()
