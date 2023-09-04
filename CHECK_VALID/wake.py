from CHECK_VALID.computer import *
import tkinter as tk


class GuiWake:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("200x300")
        self.root.iconbitmap("error")
        self.root.config(cursor="hand2")
        self.root.title("UNIKE")

        self.my_menu = tk.Menu(self.root)
        self.root.config(menu=self.my_menu)

        self.start_menu = tk.Menu(self.my_menu)
        self.my_menu.add_command(label="START ALL", command=start_all)
        self.stop_menu = tk.Menu(self.my_menu)
        self.my_menu.add_command(label="STOP ALL", command=stop_all)
        self.restart_menu = tk.Menu(self.my_menu)
        self.my_menu.add_command(label="RESTART ALL", command=restart_all)

        self.frame = tk.Frame(self.root)
        self.button_frame = tk.Frame(self.frame)

        """
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)
        self.button_frame.columnconfigure(3, weight=1)
        """
        x = tk.IntVar()
        y = tk.IntVar()
        for r in range(len(comps)):
            for c in range(2):
                label = tk.Label(self.frame, text="pc%s" % (r + 1))
                label.grid(row=r, column=0)
                rad_button1 = tk.Radiobutton(self.frame, text="Start", value=len(comps), variable=x, indicatoron=False,
                                             width=7)
                rad_button1.grid(row=r, column=c + 1)
                """
                self.rad_button2 = tk.Radiobutton(self.frame, text="Stop", value=r, variable=x, indicatoron=False, width=7)
                self.rad_button2.grid(row=r, column=2)
                self.button = tk.Button(self.frame, text="Reboot", width=7)
                self.button.grid(row=r, column=3)
                """
        """
        pc1.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC1", font=("Consolas", 10), variable=pc1.check_state)
        self.check.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame,
                             text="Wake",
                             font=("Consolas", 10),
                             command=pc1.pc_start)
        self.btn.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc1.pc_restart)
        self.btn.grid(row=0, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc1.pc_shut_down)
        self.btn.grid(row=0, column=3, sticky=tk.W + tk.E)
        self.btn.config(fg="green")

        pc2.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC2", font=("Consolas", 10), variable=pc2.check_state)
        self.check.grid(row=1, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc2.pc_start)
        self.btn.grid(row=1, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc2.pc_restart)
        self.btn.grid(row=1, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc2.pc_shut_down)
        self.btn.grid(row=1, column=3, sticky=tk.W + tk.E)

        pc3.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC3", font=("Consolas", 10), variable=pc3.check_state)
        self.check.grid(row=2, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc3.pc_start)
        self.btn.grid(row=2, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc3.pc_restart)
        self.btn.grid(row=2, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc3.pc_shut_down)
        self.btn.grid(row=2, column=3, sticky=tk.W + tk.E)

        pc4.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC4", font=("Consolas", 10), variable=pc4.check_state)
        self.check.grid(row=3, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc4.pc_start)
        self.btn.grid(row=3, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc4.pc_restart)
        self.btn.grid(row=3, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc4.pc_shut_down)
        self.btn.grid(row=3, column=3, sticky=tk.W + tk.E)

        pc5.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC5", font=("Consolas", 10), variable=pc5.check_state)
        self.check.grid(row=4, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc5.pc_start)
        self.btn.grid(row=4, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc5.pc_restart)
        self.btn.grid(row=4, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc5.pc_shut_down)
        self.btn.grid(row=4, column=3, sticky=tk.W + tk.E)

        pc6.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC6", font=("Consolas", 10), variable=pc6.check_state)
        self.check.grid(row=5, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc6.pc_start)
        self.btn.grid(row=5, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc6.pc_restart)
        self.btn.grid(row=5, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc6.pc_shut_down)
        self.btn.grid(row=5, column=3, sticky=tk.W + tk.E)

        pc7.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC7", font=("Consolas", 10), variable=pc7.check_state)
        self.check.grid(row=6, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc7.pc_start)
        self.btn.grid(row=6, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc7.pc_restart)
        self.btn.grid(row=6, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc7.pc_shut_down)
        self.btn.grid(row=6, column=3, sticky=tk.W + tk.E)

        pc8.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC8", font=("Consolas", 10), variable=pc8.check_state)
        self.check.grid(row=7, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc8.pc_start)
        self.btn.grid(row=7, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc8.pc_restart)
        self.btn.grid(row=7, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc8.pc_shut_down)
        self.btn.grid(row=7, column=3, sticky=tk.W + tk.E)

        pc9.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC9", font=("Consolas", 10), variable=pc9.check_state)
        self.check.grid(row=8, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc9.pc_start)
        self.btn.grid(row=8, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc9.pc_restart)
        self.btn.grid(row=8, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc9.pc_shut_down)
        self.btn.grid(row=8, column=3, sticky=tk.W + tk.E)
        
        pc10.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.button_frame, text="PC10", font=("Consolas", 10), variable=pc10.check_state)
        self.check.grid(row=9, column=0, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Wake", font=("Consolas", 10), command=pc10.pc_start)
        self.btn.grid(row=9, column=1, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="Restart", font=("Consolas", 10), command=pc10.pc_restart)
        self.btn.grid(row=9, column=2, sticky=tk.W + tk.E)
        self.btn = tk.Button(self.button_frame, text="S/Down", font=("Consolas", 10), command=pc10.pc_shut_down)
        self.btn.grid(row=9, column=3, sticky=tk.W + tk.E)
        """

        # self.button_frame.pack(fill="x")
        self.frame.pack(fill="x")

        self.root.mainloop()


GuiWake()
