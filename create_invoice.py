from tkinter import *
import random
import os
from tkinter import messagebox

# ==========Main Screen===========
class invoice_create:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Create Invoice")
        bg_color = "#5596e0"
        title = Label(self.root, text="Create Invoice", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#5596e0", fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # ==============Mowing============
        self.mowing = IntVar()
        self.trimming = IntVar()
        self.edging = IntVar()
        self.blowing = IntVar()
    # =============Landscape===========
        self.cleanup = IntVar()
        self.paper = IntVar()
        self.mulch = IntVar()
        self.rock = IntVar()
    # =======Total Product Price==========
        self.mowing_price = StringVar()
        self.lanscape_price = StringVar()
    # ===========Customer=================
        self.cust_name = StringVar()
        self.cust_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ==============Tax==================
        self.mowing_tax = StringVar()
        self.landscape_tax = StringVar()
    # ==========Customer Retail===========
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#5595e0")
        
        
root = Tk()
obj = invoice_create(root)
root.mainloop()