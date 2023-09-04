from wakeonlan import send_magic_packet
from tkinter import messagebox as mb
from os import system
from ping3 import ping
import time
from threading import Thread


class Computer:
    def __init__(self,
                 name,
                 mac_address,
                 ip_address,
                 dns):
        self.name = name
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.dns = dns

    def pc_start(self):
        if self.check_state.get() == 0:
            send_magic_packet(self.mac_address)
            self.check_state.set(1)
        else:
            mb.showinfo(title="NOTIFICATION", message=f"{self.name} ALREADY RUNNING")

    def pc_restart(self):
        if self.check_state.get() == 1:
            system(f"start /min net use \\\{self.name} server /user:server{self.ip_address[-2:]}")
            system(f"start /min shutdown /m \\\{self.name} /r /f /t 3")
            system(f"start /min net use * /d /y")
        else:
            mb.showinfo(title="ERROR", message=f"{self.name} NOT RUNNING")

    def pc_shut_down(self):
        if self.check_state.get() == 1:
            system(f"start /min net use \\\{self.name} server /user:server{self.ip_address[-2:]}")
            system(f"start /min shutdown /m \\\{self.name} /s /f /t 3")
            system("start /min net use * /d /y")
            self.check_state.set(0)
        else:
            mb.showinfo(title="ERROR", message=f"{self.name} NOT RUNNING")


def start_all():
    for items in comps:
        send_magic_packet(items.mac_address)


def restart_all():
    for items in comps:
        system(f"start /min net use \\\{items.name} server /user:server{items.name[-2:]}")
        system(f"start /min shutdown /m \\\{items.name} /r /f /t 3")
    system(f"start /min net use * /d /y")


def stop_all():
    for items in comps:
        system(f"start /min net use \\\{items.name} server /user:server{items.name[-2:]}")
        system(f"start /min shutdown /m \\\{items.name} /s /f /t 3")
    system(f"start /min net use * /d /y")





pc1 = Computer("PC01", "D4856494C8B1", "192.168.13.201", "255.255.255.0")
pc2 = Computer("PC02", "D8D38581B8FA", "192.168.13.202", "255.255.255.0")
pc3 = Computer("PC03", "18A9051AA645", "192.168.13.203", "255.255.255.0")
pc4 = Computer("PC04", "D48564B83659", "192.168.13.204", "255.255.255.0")
pc5 = Computer("PC05", "D8D38577E02F", "192.168.13.205", "255.255.255.0")
pc6 = Computer("PC06", "80C16EF024E1", "192.168.13.206", "255.255.255.0")
pc7 = Computer("PC07", "D48564B8367F", "192.168.13.207", "255.255.255.0")
pc8 = Computer("PC08", "D48564B83658", "192.168.13.208", "255.255.255.0")
pc9 = Computer("PC09", "082E5F1DEB42", "192.168.13.209", "255.255.255.0")
pc10 = Computer("PC10", "A0B3CCF71BE8", "192.168.13.210", "255.255.255.0")

comps = [
    pc1,
    pc2,
    pc3,
    pc4,
    pc5,
    pc6,
    pc7,
    pc8,
    pc9,
    pc10
]



'''
- start/restart shut down all pc
- change color / bold of a button and ping 
on closing shut down all // no
'''


