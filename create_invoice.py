from tkinter import *
import random
import os
from tkinter import messagebox

#==========Main Screen===========
class invoice_create:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Create Invoice")
        bg_color = "#5596e0"
        title = Label(self.root, text="Create Invoice", font=('times new roman', 30, 'bold'), pady=2 bd=12, bg="#5596e0", fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # =======variables========
        self.mowing = IntVar()
        self.mask = IntVar()
        
root = Tk()
obj = invoice_create(root)
root.mainloop()