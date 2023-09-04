# SuperFastPython.com
# example of a long-running daemon thread
from time import sleep
from threading import Thread
from ping3 import ping
from CHECK_VALID import main


# long-running background task
def background_task():

    # record the last seen value
    is_running = False
    # run forever
    while True:
        # check for change
        if ping("192.168.100.1") != "None":
            # report the change
            main.button.config(fg="green")
            print("Comp is running")
        else:

            main.button.config(fg="red")
        # block for a while
        sleep(2)


daemon = Thread(target=background_task, daemon=True)
daemon.start()

"""
# global data
data = 0
# create and start the daemon thread
print('Starting background task...')
daemon = Thread(target=background_task, daemon=True)
daemon.start()
# main thread is carrying on...
print('Main thread is carrying on...')
for _ in range(5):
    # block for a while
    value = random() * 5
    sleep(value)
    # update the data variable
    data = value
print('Main thread done.')
"""