import sqlite3
from tkinter import *
from tkinter import messagebox

signup = Tk()
signup.title("Sign Up")
signup.geometry("600x700+350+50")
signup.configure(background='#53B3CB')
signup.iconbitmap('MrCode.ico')

dbms = sqlite3.connect('MrCode.db')
cursor = dbms.cursor()
sql = "CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER PRIMARY KEY, user TEXT, password TEXT);"
cursor.execute(sql)

# Connect to database
conn = sqlite3.connect('MrCode.db')
c = conn.cursor()


# register function
def register():
    global user
    global password
    global confirm_password

    # get the values from the text boxes
    user.get()
    password.get()
    # check if the user already exists
    c.execute("SELECT * FROM customers WHERE user = :user", {'user': user.get()})
    if c.fetchall():
        messagebox.showerror('Error', 'User already exists')
    else:
        # insert the user into the database
        c.execute("INSERT INTO customers (user, password)" "VALUES (?, ?)",
                  (user.get(), password.get()))

        conn.commit()
        messagebox.showinfo('Success', 'User has been created')
        signup.destroy()

        user.set('')
        password.set('')


# main logo
label = Label(signup, text="Mr.Code Programming", width=20, height=2, justify=CENTER, font='Courier 17 bold',
              fg='#0C090D', bg="#53B3CB", )
label.pack(pady=20)

# close button
Button(signup, text="X", command=signup.destroy, bg="#fff", fg='#E01A4F', font='Courier 15 bold', width=2,
       height=1).place(x=530, y=0)
# Label
label = Label(signup, text="Sign up", justify=CENTER, font='Courier 30 bold', fg='#001B2E', bg="#53B3CB")
label.place(x=250, y=70)
# username label
label_username = Label(signup, text="Username", width=20, height=2, justify=CENTER, font='Courier 17 bold',
                       fg='#FFFFFF', bg='#53B3CB')
label_username.place(x=40, y=130)
# username entry
user = Entry(signup, width=30, bg='#fff', fg='#001B2e', font='Courier 15 bold', justify=CENTER)
user.place(x=220, y=135)


# password label
label_password = Label(signup, text="password", width=20, height=2, justify=CENTER, font='Courier 17 bold',
                       fg='#FFFFFF', bg='#53B3CB')
label_password.place(x=40, y=180)
# password entry
password = Entry(signup, width=30, show='*', bg='#fff', fg='#001B2e', font='Courier 15 bold', justify=CENTER)
password.place(x=220, y=185)

# confirm password label
label_confirm_password = Label(signup, text="confirm password", width=20, height=2, justify=CENTER,
                               font='Courier 17 bold', fg='#FFFFFF', bg='#53B3CB')
label_confirm_password.place(x=20, y=230)
# confirm password entry
confirm_password = Entry(signup, width=30, show='*', bg='#fff', fg='#001B2e', font='Courier 15 bold', justify=CENTER)
confirm_password.place(x=220, y=235)

# sign up button
Button(signup, text="Sign Up", fg='#A41623', command=register, bg='#fff', font='Courier 17 bold', width=20,
       height=2).place(x=220, y=300)

signup.mainloop()
