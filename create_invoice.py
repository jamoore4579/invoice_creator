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
        title = Label(self.root, text="Create Invoice", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg=bg_color, fg="Black", relief=GROOVE)
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
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.cust_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphone_lbl = Label(F1, text="Customer Phone:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cphone_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=15, textvariable=self.cust_phone, font='arial 15', bd=7, relief=GROOVE)
        cphone_txt.grid(row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="Bill Number:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cbill_lbl.grid(row=0, column=4, padx=20, pady=5)


        
root = Tk()
obj = invoice_create(root)
root.mainloop()