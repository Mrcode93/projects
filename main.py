from tkinter import *
from tkinter import messagebox
from datetime import *
import sqlite3


# import pyzbar.pyzbar as pyzbar
# import cv2
# import numpy as np
# from PIL import Image
# from pygments import scanner


def signIn():
    global user
    global email

    if password.get() == '' or user.get() == '':
        messagebox.showerror('Error', 'املأ الحقول رجائاً')
    else:
        # connect to database
        conn = sqlite3.connect('MrCode.db')
        c = conn.cursor()
        c.execute("SELECT * FROM customers WHERE user=? AND password=?",
                  (user.get(), password.get()))
        if c.fetchone() is None:
            messagebox.showerror('Error', 'عذراًِ كلمة المرور او اليوزر غير صحيح !')
            user.set('')
            password.set('')
        else:
            messagebox.showinfo('Success', 'تم تسجيل الدخول بنجاح')

            # open new window
            def OpenMainWidow():
                window = Toplevel(root)
                window.title('Office')
                window.geometry('1440x800')
                window.configure(background='#119DA4')

                # create a frame containing the buttons
                frame = Frame(window, bg='#02394A', width=260, height=400)
                frame.pack(side=RIGHT, fill=Y)

                # create a new database
                dbms = sqlite3.connect('office.db')
                cursor = dbms.cursor()
                sql = "CREATE TABLE IF NOT EXISTS clients (client_id INTEGER PRIMARY KEY, name TEXT, phone TEXT);"
                cursor.execute(sql)

                # Connect to database
                conn = sqlite3.connect('office.db')
                c = conn.cursor()

                # create products to data
                # create a new database
                dbms = sqlite3.connect('products.db')
                cursor = dbms.cursor()
                sql = "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, product TEXT, price TEXT, quantity TEXT);"
                cursor.execute(sql)

                # Connect to database
                conn = sqlite3.connect('products.db')
                c = conn.cursor()
                # calculate the total price in stock
                c.execute('SELECT * FROM products')
                records = c.fetchall()
                total = 0
                for row in records:
                    total += int(row[2]) * int(row[3])

                    # create a label
                    product_Label2 = Label(window, text=("المجموع", total, '$'), bg='#fff', fg='#004156',
                                           font='times 15 bold',
                                           width=30, height=2)
                    product_Label2.place(x=195, y=0)
                # create a label
                Label(window, text='مـــــذخـــــر أدويـــــة فـــــارمـــــا ', font='Tajawal 25 bold', fg='#119DA4',
                      bg='white',
                      justify=CENTER, width=30, height=2).place(x=450, y=0)

                # create a date label
                Label(window, text=datetime.now().strftime('%A %d %b %Y'), font='Tajawal 15 bold', fg='#119DA4',
                      bg='white',
                      justify=CENTER, width=30, height=2).place(x=1210, y=0)

                # # menu bar
                # menubar = Menu(window)
                # f = Menu(menubar, tearoff=0)
                # f.add_command(label="New")
                # f.add_command(label="new file")
                # f.add_command(label=open)
                # f.add_command(label="save")
                # f.add_command(label='save as')
                # f.add_command(label='Exit')
                # window.config(menu=menubar)

                # open bill
                def openBill():
                    import products

                #####=========================================show data in stock=======================================================
                # show data in the database
                def showData():
                    # create a new window
                    window3 = Toplevel(window)
                    window3.title('عرض المادة')
                    window3.geometry('500x400')
                    window3.configure(background='#119DA4')

                    # create a scrollbar
                    scrollbar = Scrollbar(window3)
                    scrollbar.pack(side=LEFT, fill=Y)

                    # create a listbox
                    listbox = Listbox(window3, yscrollcommand=scrollbar.set)
                    listbox.pack(side=LEFT, fill=BOTH)

                    # show data in the listbox
                    c.execute("SELECT * FROM products")
                    for row in c.fetchall():
                        listbox.insert(END, row)

                ########======================================Search fo item============================================================
                # search box
                def search():
                    connection = sqlite3.connect('products.db')
                    cur = connection.cursor()
                    cur.execute("SELECT product FROM products WHERE product =?", (z.get(),))
                    connection.commit()
                    variablename = cur.fetchall()

                    # if the product is not in database
                    if not variablename:
                        # global product_label
                        messagebox.showinfo("خطأ", 'المادة غير موجودة في المذخر')
                        search_entry.delete(0, END)
                    else:
                        # show the product and the quantity
                        cur.execute("SELECT product FROM products WHERE product =?", (z.get(),))
                        variablename = cur.fetchall()
                        # get the quantity of variablename form database
                        cur.execute("SELECT quantity FROM products WHERE product =?", (z.get(),))
                        quantity = cur.fetchall()
                        # show the product and the quantity

                        Label(window, text=(variablename, ':', quantity), font='Tajawal 15 bold', fg="#119da4",
                              bg='white',
                              justify=CENTER, width=20,
                              height=2).place(x=970, y=0)
                        z.set("")

                z = StringVar()

                ####===================================!Add item============================================================
                def addProducts():
                    # create a new window
                    window5 = Toplevel(window)
                    window5.title('إضافة مواد')
                    window5.geometry('700x600')
                    window5.configure(background='#119DA4')

                    product = StringVar()
                    price = StringVar()
                    quantity = StringVar()
                    # create a label
                    Label(window5, text='إضافة مواد', font="Tajawal 25 bold", fg='#ffffff', bg='#F85C50',
                          justify=CENTER, width=30,
                          height=2).pack()
                    # name
                    Label(window5, text="المادة", font='Tajawal 25 bold', fg='#ffffff', bg='#F85C50',
                          justify=CENTER).place(x=555,
                                                y=120)
                    Entry(window5, textvariable=product, font='Tajawal 20 bold', fg='#F85C50', bg='#ffffff',
                          justify=CENTER).place(
                        x=200,
                        y=120)
                    # phone
                    Label(window5, text=" السعر", font='Tajawal 25 bold', fg='#ffffff', bg='#F85C50',
                          justify=CENTER).place(x=555,
                                                y=180)
                    Entry(window5, textvariable=price, font='Tajawal 20 bold', fg='#F85C50', bg='#ffffff',
                          justify=CENTER).place(
                        x=200, y=180)

                    # quantity
                    Label(window5, text=" العدد", font='Tajawal 25 bold', fg='#ffffff', bg='#F85C50',
                          justify=CENTER).place(x=555,
                                                y=250)
                    Entry(window5, textvariable=quantity, font='Tajawal 20 bold', fg='#F85C50', bg='#ffffff',
                          justify=CENTER).place(
                        x=200, y=250)

                    # add product to database
                    def addProducts2():
                        product.get()
                        price.get()
                        quantity.get()

                        if product.get() == '' or price.get() == '' or quantity.get() == '':
                            messagebox.showinfo('خطأ', 'يرجى ادخال البيانات')

                        else:

                            # if the product is in the database add the quantity to the existing quantity
                            c.execute("SELECT * FROM products WHERE product =?", (product.get(),))
                            conn.commit()
                            variablename = c.fetchall()
                            if variablename:
                                # add the new quantity to the old quantity in database
                                connection = sqlite3.connect('products.db')
                                cur = connection.cursor()
                                cur.execute("SELECT quantity FROM products", )

                                old = cur.fetchall()
                                old1 = int(old[0][0])
                                new = int(quantity.get())
                                new1 = old1 + new

                                cur.execute("UPDATE products SET quantity = ? WHERE product =?", (new1, product.get()))

                                # cur.execute("UPDATE products SET quantity WHERE quantity", (newOne,))

                                connection.commit()
                                messagebox.showinfo('تم', 'تمت الاضافة بنجاح')
                                product.set('')
                                price.set('')
                                quantity.set('')
                            else:
                                # insert the user into the database
                                c.execute('INSERT INTO products (product, price, quantity) VALUES (?, ?, ?)',
                                          (product.get(), price.get(),
                                           quantity.get()))

                                conn.commit()
                                messagebox.showinfo('تم', 'تمت الاضافة بنجاح')
                                product.set('')
                                price.set('')

                    # button
                    Button(window5, text="إضافة", font='Tajawal 18 bold', fg='#F85C50', bg='white', justify=CENTER,
                           width=10,
                           height=2,
                           command=addProducts2).place(x=200, y=300)

                ###================================================Open Bill============================================================
                Button(window, text='فتح فاتورة', font='Tajawal 18 bold', fg='#119DA4', bg='white', justify=CENTER,
                       width=20, height=2, command=openBill).place(x=1200, y=140)

                # create a button
                Button(window, text='عرض المواد', command=showData, font='Tajawal 18 bold', fg='#119DA4', bg='white',
                       width=20,
                       height=2).place(x=1200, y=200)

                # create a button to exit the program
                Button(window, text="خروج", font="Tajawal 15 bold", fg='#EE3D48', bg='white', justify=CENTER, width=10,
                       height=2,
                       command=window.destroy).place(x=0, y=0)
                # create a search button
                Button(window, text='بحث', font='Tajawal 18 bold', fg='#119DA4', bg='white', justify=CENTER, width=10,
                       command=search).place(x=1250, y=60)
                # create an Entry beside the search button
                search_entry = Entry(window, width=30, textvariable=z, font='Tajawal 15 bold', bg='#fff', fg='#004156')
                search_entry.place(x=1200, y=100)
                # create add products the sales
                Button(window, text='اضافة مادة', font='Tajawal 18 bold', fg='#119DA4', bg='white', justify=CENTER,
                       width=20, height=2, command=addProducts).place(x=1200, y=260)

                # function to add the debts
                def debts():
                    # create a new window
                    window6 = Toplevel(window)
                    window6.title('الديون')
                    window6.geometry('1366x768+0+0')
                    window6.configure(bg='#119da4')
                    # create a label
                    Label(window6, text='الــديــون', font='Tajawal 30 bold', fg='#119da4', bg='white', width=40).place(
                        x=360, y=0)
                    # create a label
                    Label(window6, text='الاســــم', font='Tajawal 18 bold', fg='#119da4', bg='white', width=15).place(
                        x=1160, y=200)
                    # create a label
                    Label(window6, text='الـمـبلـغ', font='Tajawal 18 bold', fg='#119da4', bg='white', width=15).place(
                        x=1000, y=200)
                    # create a frame
                    frame = Frame(window6, width=450, height=600, bg='#4C1A57').place(x=100, y=100)
                    # create a label
                    Label(window6, text='إضافة دَين', font='Tajawal 18 bold', fg='#4C1A57', bg='white', width=15,
                          height=2).place(
                        x=230, y=100)
                    # create a label
                    Label(window6, text='الاســم', font='Tajawal 18 bold', fg='#4C1A57', bg='white', width=20,
                          height=2).place(
                        x=200, y=200)
                    # create a label
                    Label(window6, text='المبلغ', font='Tajawal 18 bold', fg='#4C1A57', bg='white', width=20,
                          height=2).place(
                        x=200, y=350)

                    # crete a function to add debts to database
                    def Save_debt():

                        # create new database
                        dbd = sqlite3.connect('debts.db')
                        # create cursor
                        cursor = dbd.cursor()
                        # create a table
                        cursor.execute("CREATE TABLE IF NOT EXISTS debts(name TEXT , amount INTEGER)")
                        # create a variable to get the name
                        name = name_entry.get()
                        # create a variable to get the amount
                        amount = amount_entry.get()
                        # insert the data to the tabel debts
                        if name == "" or amount == "":
                            messagebox.showinfo('خطأ', "يرجى ملئ الحقول")

                        else:
                            # check if name is already in the database
                            cursor.execute("SELECT * FROM debts WHERE name =?", (name,))
                            # create a variable to get the data
                            data = cursor.fetchall()
                            # check if name is already in the database
                            if len(data) != 0:
                                messagebox.showinfo("الاسم موجود مسبقاً سيتم اضافة المبلغ فقط")
                                # add the just amount th the same name
                                cursor.execute("UPDATE debts SET amount = amount +? WHERE name =?", (amount, name))
                                # commit changes
                                dbd.commit()
                            else:
                                cursor.execute("INSERT INTO debts(name,amount) VALUES(?, ?)", (name, amount))
                                # commit the changes
                                dbd.commit()
                                messagebox.showinfo("تم", "تمت اضافة الدين")
                        name = ""
                        amount = ""
                    # create search function
                    def search():
                        # search for the name in database
                        names = the_name.get()
                        # connect to the database
                        connection = sqlite3.connect('debts.db')
                        cur = connection.cursor()
                        cur.execute("SELECT * FROM debts WHERE name =?", (names,))
                        connection.commit()
                        data = cur.fetchall()
                        # get the amount of the name
                        amount = data[0][1]

                        #check if name in database
                        if len(data) == 0:
                            messagebox.showerror("خطأ", "الاسم غير موجود")
                        else:
                            # create  a Label to show the name and amount
                            Label(window6, text=(names + " : " + str(amount)), font='Tajawal 18 bold', fg='#119da4',
                                  bg="#fff", width=30, height=2, justify=CENTER).place(x=1000, y=145)

                    the_name =StringVar()
                    # create search entry
                    Label(window6, text="الاســم",font='Tajawal 18 bold', fg='#119da4', bg="#fff", width=40, height=2).place(x=1000, y=50)
                    Entry(window6, textvariable=the_name,font='Tajawal 18 bold', fg='#119da4', bg="#fff", width=20 ).place(x=1150, y=100)
                    Button(window6, text="بحث",font='Tajawal 18 bold', fg='#119da4', bg="#fff", width=10, height=1,command=search).place(x=1000,y=100)




                    name_entry = StringVar()
                    amount_entry = StringVar()
                    # create an entry
                    Entry(window6, width=20, textvariable=name_entry, font='Tajawal 15 bold', bg='#fff',
                          justify=CENTER).place(x=220, y=270)
                    # create an entry
                    Entry(window6, width=20, textvariable=amount_entry, font='Tajawal 15 bold', bg='#fff',
                          justify=CENTER).place(x=220, y=420)

                    # create a button
                    Button(window6, text='حــفـــظ', font='Tajawal 18 bold', fg='#4C1A57', bg='white', width=20,
                           height=2, command=Save_debt).place(x=180, y=480)

                Button(window, text='الديون', font='Tjawal 18 bold', fg='#119da4', bg='#fff', width=20, height=2,
                       command=debts).place(x=1200, y=380)

                # update the window every 5 seconds
                def update():
                    now = datetime.now()
                    time = now.strftime('%H:%M:%S')
                    window.after(1000, update)
                    time_label = Label(window, text=time, font='Tajawal 15 bold', fg='#119DA4', bg='white',
                                       justify=CENTER, width=9,
                                       height=2)
                    time_label.place(x=1180, y=0)

                update()

                ####======================================================Show sales========================================================
                def showSales():
                    # create a window
                    sales = Toplevel(window)
                    sales.title('عرض المبيعات')
                    sales.geometry('1366x768')
                    sales.config(background='#119DA4')
                    # create a label
                    Label(sales, text='عرض المبيعات', font='Tajawal 18 bold', fg='#119DA4', bg='white',
                          justify=CENTER, width=20, height=2).pack(pady=0)
                    # create a scrollbar
                    scrollbar = Scrollbar(sales)
                    scrollbar.pack(side=RIGHT, fill=Y)
                    # create a listbox

                # create a button to show the sales
                Button(window, text="عرض المبيعات", font='Tajawal 18 bold', fg='#119DA4', bg='white',
                       justify=CENTER, width=20, height=2, command=showSales).place(x=1200, y=320)

        OpenMainWidow()
        user.set('')
        password.set('')


# ======================================================Login===========================================================

def close():
    root.destroy()


root = Tk()
root.title('Sign In')
root.geometry('800x650+350+50')
root.configure(background='#276FBF')
user = StringVar()
email = StringVar()
password = StringVar()

# add to database
dbms = sqlite3.connect('MrCode.db')
cursor = dbms.cursor()
sql = "CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER PRIMARY KEY, user TEXT,  password TEXT);"
cursor.execute(sql)
# main logo
label = Label(root, text="اهلاً بكم في مذخر فــــارمـــــا", width=30, height=2, justify=CENTER, font='Tajawal 30 bold',
              fg='#119DA4', bg="#fff")
label.pack(pady=20)

label = Label(root, text="تسجــيــل الـدخول", justify=CENTER, font='Tajawal 25 bold', fg='#FFF')
label.configure(background="#276FBF")
label.pack(pady=50)

Label(root, text="اليوزر ", justify=CENTER, font='Tajawal 20 ', fg='#F6F4F3', bg='#276FBF').place(x=560, y=220)

Label(root, text="كلمة المرور ", justify=CENTER, font='Tajawal 20 ', fg='#F6F4F3', bg='#276FBF').place(x=560, y=260)

Entry(root, width=20, font='Tajawal 20 bold', textvariable=user, fg='black', bg='#F6F4F3', justify=CENTER).place(x=260,
                                                                                                                 y=220)

Entry(root, width=20, font='Tajawal 20 bold', textvariable=password, show='*', fg='black', bg='#F6F4F3',
      justify=CENTER).place(x=260,
                            y=260)

Button(root, text="تسجيل دخول", width=20, height=2, font='Tajawal 20 bold', fg='#276FBF', bg='blue',
       command=signIn, justify=CENTER).place(x=250,
                                             y=350)

# validateLogin = partial(signIn, user, email, password)

Button(root, text="إغلاق", width=8, height=2, font='Tajawal 15 bold', borderwidth=1, fg='red', bg='#ffffff',
       command=close, justify=CENTER).place(x=695, y=0)

root.mainloop()
