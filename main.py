from tkinter import *


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
    tk.withdraw()
    

tk = Tk()
tk.geometry('250x300')
tk.title('WakeOnLan')

render_main_view()
tk.mainloop()
