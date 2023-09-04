import tkinter as tk

def click():


root = tk.Tk()

frame = tk.Frame(root)


#pc1
label_1 = tk.Label(frame, text="PC1")
label_1.grid(row=0, column=0)
btn_1 = tk.Button(frame, text="", command=pc1.click)




frame.pack(fill="x")
root.geometry("200x300")




root.mainloop()