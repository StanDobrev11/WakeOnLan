from threading import Thread
import time
from wakeonlan import send_magic_packet
from os import system
from ping3 import ping
import tkinter as tk
from collections import defaultdict


class Computer:
    def __init__(self, name, mac_address, ip_address):
        self.name = name
        self.mac_address = mac_address
        self.ip_address = ip_address


pc1 = Computer("PC01", "D4856494C8B1", "192.168.100.1")
pc2 = Computer("PC02", "D8D38581B8FA", "192.168.13.202")
pc3 = Computer("PC03", "18A9051AA645", "192.168.13.203")
pc4 = Computer("PC04", "D48564B83659", "192.168.13.204")
pc5 = Computer("PC05", "D8D38577E02F", "192.168.13.205")
pc6 = Computer("PC06", "80C16EF024E1", "192.168.13.206")
pc7 = Computer("PC07", "D48564B8367F", "192.168.13.207")
pc8 = Computer("PC08", "D48564B83658", "192.168.13.208")
pc9 = Computer("PC09", "082E5F1DEB42", "192.168.13.209")
pc10 = Computer("PC10", "A0B3CCF71BE8", "192.168.13.210")

comps = ["pc1", "pc2", "pc3", "pc4", "pc5", "pc6", "pc7", "pc8", "pc9", "pc10"]
comps_int = [pc1, pc2, pc3, pc4, pc5, pc6, pc7, pc8, pc9, pc10]

#board = [[ping(comps_int.ip_address) for b in range(1)] for a in range(len(comps))]
buttons = defaultdict(lambda: None)



def background_list():
    global board
    btn = buttons[row, col]
    while True:
        start = time.perf_counter()
        board = [ping(pc1.ip_address),
                 ping(pc2.ip_address),
                 ping(pc3.ip_address),
                 ping(pc4.ip_address),
                 ping(pc5.ip_address),
                 ping(pc6.ip_address),
                 ping(pc7.ip_address),
                 ping(pc8.ip_address),
                 ping(pc9.ip_address),
                 ping(pc10.ip_address)
                 ]
        end = time.perf_counter()
        if board[0] is not None:
            btn.config(fg="yellow")
        print(f"{end - start} sec")
        #board[0] = ping(pc1.ip_address)
        #board[1] = ping(pc2.ip_address)
        print(board)
            #board.append(ping(comp.ip_address))
            #if len(board) == 11:
            #    board = []
            #count += 1
            #print(count)
            #print(board)



def click(self, row, col):
    btn = buttons[row, col]
    if ping(f"{self.ip_address}") is None:
        send_magic_packet(self.mac_address)
        btn.config(text="STARTED", fg="green")
        print(self.mac_address)
    else:
        #system(f"start /min net use \\\{self.ip_address} 123456 /user:sway")
        #system(f"start /min shutdown /m \\\{self.ip_address} /s /f /t 3")
        system(f"start /min net use \\\{self.name} server /user:server{self.ip_address[-2:]}")
        system(f"start /min shutdown /m \\\{self.name} /s /f /t 3")
        system("start /min net use * /d /y")
        btn.config(text="STOPPED", fg="red")
        #print(f"{self.name} Stopped")
        #print(ping(f"{self.ip_address}"))

##def btn_color(self, row, col):
    #global board
    #while board[0] is not None:
        #btn.config(fg="yellow")
        #btn = buttons[row, col]


def pc_restart(self):
    system(f"start /min net use \\\{self.name} server /user:server{self.ip_address[-2:]}")
    system(f"start /min shutdown /m \\\{self.name} /r /f /t 3")
    system(f"start /min net use * /d /y")
    print(f"{self.name}")

def start_all():
    for items in comps_int:
        send_magic_packet(items.mac_address)


def restart_all():
    for items in comps_int:
        system(f"start /min net use \\\{items.name} server /user:server{items.name[-2:]}")
        system(f"start /min shutdown /m \\\{items.name} /r /f /t 3")
    system(f"start /min net use * /d /y")


def stop_all():
    for items in comps_int:
        system(f"start /min net use \\\{items.name} server /user:server{items.name[-2:]}")
        system(f"start /min shutdown /m \\\{items.name} /s /f /t 3")
    system(f"start /min net use * /d /y")


"""
def pc_start(self, row, col):
    btn_start = buttons[row, col]
    btn_start.config(text=f"{self.name} Started", fg="green")
    send_magic_packet(self.mac_address)
    print(self.mac_address)
    if ping(f"{self.ip_address}") is not None or False:
        pc_stop(self)
        btn_start.config(text=f"{self.name} Stopped", fg="red")


def pc_stop(self):
    system(f"start /min net use \\\{self.ip_address} 123456 /user:sway")
    system(f"start /min shutdown /m \\\{self.ip_address} /s /f /t 3")
    # system(f"start /min net use \\\{self.name} server /user:server{self.ip_address[-2:]}")
    # system(f"start /min shutdown /m \\\{self.name} /s /f /t 3")
    system("start /min net use * /d /y")
    print(f"{self.name} Stopped")
"""


class Gui:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("400x400")

        self.my_menu = tk.Menu(self.root)
        self.root.config(menu=self.my_menu)

        self.start_menu = tk.Menu(self.my_menu)
        self.my_menu.add_command(label="START ALL", command=start_all)
        self.stop_menu = tk.Menu(self.my_menu)
        self.my_menu.add_command(label="STOP ALL", command=stop_all)
        self.restart_menu = tk.Menu(self.my_menu)
        self.my_menu.add_command(label="RESTART ALL", command=restart_all)

        for num in range(len(comps)):
            label = tk.Label(self.root, text="pc%s" % (num + 1))
            label.grid(row=num, column=0)

        for row in range(len(comps_int)):
            col = 1
            btn = tk.Button(self.root,
                            text=f"pc{row+1}",
                            command=lambda row=row, col=col: click(comps_int[row], row, col),
                            width=10
                            )

            btn.grid(row=row, column=col)
            buttons[row, col] = btn

            for row in range(len(comps_int)):
                col = 2
                btn_1 = tk.Button(self.root,
                                text="RESTART",
                                command=lambda row=row, col=col: pc_restart(comps_int[row]),
                                width=10
                                )

                btn_1.grid(row=row, column=col)
                buttons[row, col] = btn_1

            """
            def background_ping(self):
                while True:
                    if ping(f"{self.ip_address}") is not None or False:
                        btn_start = buttons[row, col]
                        btn_start.config(text=f"{self.name} Stopped", fg="red")
                        print(self.ip_address)
                    else:
                        btn_start = buttons[row, col]
                        btn_start.config(text=f"{self.name} Started", fg="green")
                    time.sleep(3)

            for pc in comps_int:
                threading.Thread(target=background_ping, daemon=True, args=(pc, )).start()
                time.sleep(1)
            """


        self.root.mainloop()



daemon = Thread(target=background_list, daemon=True)
daemon.start()
Thread(target=btn_color(pc1, 0, 1), daemon=True, args=(pc1, )).start()

Gui()
#print(ping ("192.168.100.50"))
#print(ping("192.168.13.201"))
#print(ping("192.168.100.1"))

"""
def background_task(pc):
    count = 0

    while True:

        print(f"{pc.ip_address}")
        btn_start = tk.Button(root, text=f"Start PC{num+1}")
        btn_start.grid(row=num, column=1)
        # else:
        # count += 1
        # print(count)


for pc in comps_int:
    print(pc)
    threading.Thread(target=background_task, args=(pc,)).start()
    time.sleep(1)
"""



