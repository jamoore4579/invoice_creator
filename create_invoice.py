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
        title = Label(self.root, text="Create Invoice", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg=bg_color, fg="black", relief=GROOVE)
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
        self.landscape_price = StringVar()
    # ===========Customer=================
        self.cust_name = StringVar()
        self.cust_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    
    # ==========Customer Retail===========
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="black", bg=bg_color)
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
        F2 = LabelFrame(self.root, text="Mowing Services", font=('times new roman', 15, 'bold'), bd=10, fg="black", bg=bg_color)
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
        F3 = LabelFrame(self.root, text="Landscaping Services", font=('times new roman', 15, 'bold'), bd=10, fg="black", bg=bg_color)
        F3.place(x=440, y=180, width=440, height=380)

        cleanup_lbl = Label(F3, text="Clean-up", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        cleanup_lbl.grid(row=0, column=2, padx=10, pady=10, sticky='W')
        cleanup_txt = Entry(F3, width=10, textvariable=self.cleanup, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        cleanup_txt.grid(row=0, column=3, padx=10, pady=10)

        paper_lbl = Label(F3, text="Paper", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        paper_lbl.grid(row=1, column=2, padx=10, pady=10, sticky='W')
        paper_txt = Entry(F3, width=10, textvariable=self.paper, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        paper_txt.grid(row=1, column=3, padx=10, pady=10)

        mulch_lbl = Label(F3, text="Mulch", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        mulch_lbl.grid(row=2, column=2, padx=10, pady=10, sticky='W')
        mulch_txt = Entry(F3, width=10, textvariable=self.mulch, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mulch_txt.grid(row=2, column=3, padx=10, pady=10)

        rock_lbl = Label(F3, text="Rock", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        rock_lbl.grid(row=3, column=2, padx=10, pady=10, sticky='W')
        rock_txt = Entry(F3, width=10, textvariable=self.rock, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rock_txt.grid(row=3, column=3, padx=10, pady=10)

    # ==========================Bill Area=========================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=880, y=180, width=470, height=380)

        bill_title = Label(F5, text="Customer Invoice", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
    
    # ========================Button Frame========================
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="black", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Mowing Price", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.mowing_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Landscaping Price", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m2_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.landscape_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=0, column=3, padx=18, pady=1)

    # =======================Buttons==============================
        btn_frame = Frame(F6, bd=7, relief=GROOVE)
        btn_frame.place(x=760, width=580, height=105)

        total_btn = Button(btn_frame, command=self.total, text="Total", bg=bg_color, bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_frame, command=self.bill_area, text="Generate Bill", bd=2, bg=bg_color, fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_frame, command=self.clear_data, text="Clear", bg=bg_color, bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_frame, command=self.exit_app, text="Exit", bd=2, bg=bg_color, fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

# =========================Total Bill=========================
    def total(self):
        self.mowing_price_fm = self.mowing.get()*50
        self.trimming_price_fm = self.trimming.get()*10
        self.edging_price_fm = self.edging.get()*5
        self.blowing_price_fm = self.blowing.get()*5
        self.total_mowing_price = float(self.mowing_price_fm+self.trimming_price_fm+self.edging_price_fm+self.blowing_price_fm)

        self.cleanup_price_fm = self.cleanup.get()*60
        self.paper_price_fm = self.paper.get()*10
        self.mulch_price_fm = self.mulch.get()*30
        self.rock_price_fm = self.rock.get()*40
        self.total_landscape_price = float(self.cleanup_price_fm+self.paper_price_fm+self.mulch_price_fm+self.rock_price_fm)
        
        self.total_bill = float(self.total_mowing_price+self.total_landscape_price)

# =======================Invoice=========================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWe Care Moore Invoice")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.cust_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.cust_phone.get()}")
        self.txtarea.insert(END, f"\n=====================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

# ====================Bill Area==========================
    def bill_area(self):
        if self.cust_name.get() == " " or self.cust_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are a Must")
        elif self.mowing_price.get() == "Rs. 0.0" and self.landscape_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()

    # ==================Mowing=======================
        if self.mowing.get() != 0:
            self.txtarea.insert(END, f"\n Mowing\t\t{self.mowing.get()}\t\t{self.mowing_price_fm}")
        if self.trimming.get() != 0:
            self.txtarea.insert(END, f"\n Trimming\t\t{self.trimming.get()}\t\t{self.trimming_price_fm}")
        if self.edging.get() != 0:
            self.txtarea.insert(END, f"\n Edging\t\t{self.edging.get()}\t\t{self.edging_price_fm}")
        if self.blowing.get() != 0:
            self.txtarea.insert(END, f"\n Blowing\t\t{self.blowing.get()}\t\t{self.blowing_price_fm}")

    # ================Landscape======================
        if self.cleanup.get() != 0:
            self.txtarea.insert(END, f"\n Cleanup\t\t{self.cleanup.get()}\t\t{self.cleanup_price_fm}")
        if self.paper.get() != 0:
            self.txtarea.insert(END, f"\n Paper\t\t{self.paper.get()}\t\t{self.paper_price_fm}")
        if self.mulch.get() != 0:
            self.txtarea.insert(END, f"\n Mulch\t\t{self.mulch.get()}\t\t{self.mulch_price_fm}")
        if self.rock.get() != 0:
            self.txtarea.insert(END, f"\n Rock\t\t{self.rock.get()}\t\t{self.rock_price_fm}")
            self.txtarea.insert(END, f"\n--------------------------------------")

            self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs.{self.total_bill}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.save_bill()
        
    
# ====================Save Bill====================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
            return

# ===================Find Bill======================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present =="no":
            messagebox.showerror("Error", "Invalid Bill No")
    
# ===============Clear Bill===================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.mowing.set(0)
            self.trimming.set(0)
            self.edging.set(0)
            self.blowing.set(0)
            # ======================
            self.cleanup.set(0)
            self.paper.set(0)
            self.mulch.set(0)
            self.rock.set(0)
            # ============================
            self.mowing_price.set("")
            self.landscape_price.set("")
            # ============================
            self.cust_name.set("")
            self.cust_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            # ============================
            self.search_bill.set("")
            self.welcome_bill()

# ===============Exit==============================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


        
root = Tk()
obj = invoice_create(root)
root.mainloop()