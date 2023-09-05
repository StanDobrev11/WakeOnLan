from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry

def clear_view():
    for slave in tk.grid_slaves():
        slave.destroy()


def render_main_view():
    Button(text='START', bg='green', fg='red').grid(row=0, column=0, padx=20, pady=20)
    Button(text='STOP', bg='red', fg='green').grid(row=1, column=0, padx=20, pady=20)
    menu = Menu()
    tk.config(menu=menu)
    menu.add_command(label="Settings", command=render_settings_window)


def render_settings_window():
    set_win = Toplevel()
    set_win.geometry('500x500')
    set_win.title('Settings')
    Label(set_win, text='Enter computer name: ').grid(row=0, column=0)
    Entry(set_win).grid(row=0, column=1)
    Label(set_win, text='DUE DATE: ').grid(row=1, column=0)
    DateEntry(set_win).grid(row=1, column=1)


    Button(set_win, text="OK").grid(row=10, column=0)
    Button(set_win, text="Cancel").grid(row=10, column=1)

    tk.withdraw()

    # tk.deiconify()


tk = Tk()
tk.geometry('250x300')
tk.title('WakeOnLan')

render_main_view()
tk.mainloop()
