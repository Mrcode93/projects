import random
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import sqlite3

# create a product window
# create a window
product_window = Tk()
product_window.title('Products')
product_window.geometry('900x900')
product_window.configure(background='#004156')


# create a label
product_Label = Label(product_window, text='الــــمــــواد', bg='#fff', fg='#004156', font='Tajawal 20 bold', width=20,
                      height=2)
product_Label.place(x=400, y=0)

# create a button


def Add():
    global name_entry
    Name = StringVar()

    # date = date.strftime('%Y-%m-%d')
    billarea = Frame(product_window, bd=10, relief=GROOVE, bg="#004156")
    billarea.place(x=100, y=80, width=530, height=672)

    scrol_y = Scrollbar(billarea, orient=VERTICAL)
    txtarea = Text(billarea, yscrollcommand=scrol_y.set,fg="#004156", bg="#fff", font='Tajawal 15 bold')
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH, expand=1)
    txtarea.delete(1.0, END)
    txtarea.insert(END, "\t\t\tمــــــذخــــــــر فـــــــــارمـــــــــا")
    txtarea.insert(END, f"\n\n\t\t\t\t رقم القائمة:{random.randint(1, 500)} ")
    txtarea.insert(END, f"\n\n\t\t\t\t  : اسم العميل ")
    txtarea.insert(END, f"\n\n\t\t\t تاريخ القائمة : {datetime.now().strftime('%A %d %b %Y')}")
    txtarea.insert(END, "\n==============================================================\n")
    txtarea.insert(END, "\n\tالسعر\t\tالعدد\t\tالمادة\n")
    txtarea.insert(END, "\n==============================================================\n")

    def add_to_bill():

        # get the name of the product
        product_name = product_name_entry.get()
        # check if the product is in the database
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products WHERE product=?", (product_name,))
        if c.fetchone() is None:
            messagebox.showerror('Error', 'المادة غير موجودة')
        else:
            # get the price of the product
            c.execute("SELECT price FROM products WHERE product=?", (product_name,))
            conn.commit()
            product_price = c.fetchone()
            # get the quantity of the product
            product_quantity = product_quantity_entry.get()
            # get the total price of the product
            product_total_price = int(product_price[0]) * int(product_quantity)
            # get the product name
            product_name = product_name_entry.get()
            # add to bill
            print(product_name)
            print(product_price)
            txtarea.insert(END, f"\n\t{product_total_price}\t\t{product_quantity}\t\t{product_name}")
        # print(name_entry.get())
        product_name_entry.delete(0, END)
        product_quantity_entry.delete(0, END)


    # create a function to save the bill
    def save_bill():
        # get the bill text
        bill_text = txtarea.get(1.0, END)
        # add total price in the bill
        txtarea.insert(END, "\n==============================================================\n")
        # calculate hte total price of items in the bill and insert it in the bill
        # total_price = 0
        # # # create a loop
        # # get the price of the all the items in the bill and calculate the total price
        # for i in range(2, txtarea.index('end')):
        #     price = txtarea.get(i, i + 1)
        #     total_price += int(price.split()[0])
        #     txtarea.insert(END,"\n==============================================================\n")
        #     txtarea.insert(END, f"\n {total_price}")
            
            
        











        # save the bill every time the button of save bill is clicked with different name
        file = open(f"bill{random.randint(1, 500)}.txt", 'w')
        file.write(bill_text)
        file.close()
        messagebox.showinfo("Success", "The file has been saved")
        # save the bill as ajson file in new database
        # create new database
        dbms = sqlite3.connect('bills.db')
        # create cursor
        cursor = dbms.cursor()
        # create tabel and save the bill as json file
        cursor.execute("CREATE TABLE IF NOT EXISTS bills (bill_text TEXT)")
        cursor.execute("INSERT INTO bills VALUES (?)", (bill_text,))
        dbms.commit()




    Label(product_window, text='المادة', bg='#004156', fg="#fff", font='Tajawal 15 bold', width=20,
          justify=CENTER).place(x=650, y=200)
    product_name_entry = Entry(product_window, bg='#fff', fg="#004156", font='Tajawal 15 bold', width=20,
                               justify=CENTER)
    product_name_entry.place(x=650, y=230)

    # create a for add product quantity entry
    Label(product_window, text='العدد', bg='#004156', fg="#fff", font='Tajawal 15 bold', width=20,
          justify=CENTER).place(x=650, y=280)
    product_quantity_entry = Entry(product_window, bg='#fff', fg="#004156", font='Tajawal 15 bold', width=20,
                                   justify=CENTER)
    product_quantity_entry.place(x=650, y=300)
    # create a button to add to bill
    add_to_bill = Button(product_window, text="Add", command=add_to_bill, bg='#fff', fg="#004156",
                         font='Tajawal 15 bold', width=10, height=1, justify=CENTER)
    add_to_bill.place(x=650, y=350)
    add_to_bill = Button(product_window, text="Save", command=save_bill, bg='#fff', fg="#004156",
                         font='Tajawal 15 bold', width=10, height=1, justify=CENTER)
    add_to_bill.place(x=650, y=400)


Button(product_window, text='فاتورة جديدة', bg='#fff', fg='#004156', font='Tajawal 15 bold', width=20, height=2,
       command=Add).place(x=700, y=0)


product_window.mainloop()
