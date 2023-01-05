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
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
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
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        cbill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)
    # ==============Mowing=================
        F2 = LabelFrame(self.root, text="Mowing Services", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F2.place(x=0, y=180, width=440, height=380)

        mowing_lbl = Label(F2, text="Mowing", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        mowing_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        mowing_txt = Entry(F2, width=10, textvariable=self.mowing, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mowing_txt.grid(row=0, column=1, padx=10, pady=10)

        trimming_lbl = Label(F2, text="Trimming", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        trimming_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        trimming_txt = Entry(F2, width=10, textvariable=self.trimming, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        trimming_txt.grid(row=1, column=1, padx=10, pady=10)

        edging_lbl = Label(F2, text="Edging", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        edging_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        edging_txt = Entry(F2, width=10, textvariable=self.edging, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        edging_txt.grid(row=2, column=1, padx=10, pady=10)

        blowing_lbl = Label(F2, text="Blowing", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        blowing_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        blowing_txt = Entry(F2, width=10, textvariable=self.edging, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        blowing_txt.grid(row=3, column=1, padx=10, pady=10)

    # ==============Landscaping============
        F3 = LabelFrame(self.root, text="Landscaping Services", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F3.place(x=440, y=180, width=440, height=380)
    # =========================Find Bill==========================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")


        
root = Tk()
obj = invoice_create(root)
root.mainloop()