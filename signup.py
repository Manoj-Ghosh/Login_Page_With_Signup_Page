from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql



def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)



def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')

    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')

    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')

    else:
        try:


            con = pymysql.connect(host= 'localhost', user='root', password='1234')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        
        try:


            query = 'create database userdata'
            mycursor.execute(query)

            query = 'use userdata'
            mycursor.execute(query)

            query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(80), password varchar(20))'
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata')

        
        query = 'select * from data where username = %s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exists')

        else:



            query = 'insert into data(email, username, password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import signin












def login_page():
    signup_window.destroy()
    import signin




signup_window = Tk()

signup_window.title('Signup Page')
signup_window.resizable(False, False)
background = ImageTk.PhotoImage(file = 'background.jpg')


bglabel = Label(signup_window, image = background)
bglabel.grid()

frame = Frame(signup_window) #frame = Frame(signup_window, width = 50, height= 20, bg= 'red')
frame.place(x = 453, y = 40)


heading = Label(frame, text = 'Create An Account', font = ('Arial',23)
                , bg = 'white', fg = 'firebrick', background= 'white')
heading.grid(row = 0, column=0, padx = 18, pady=10)

emaillabel = Label(frame, text = 'Email', font = ('Arial',10), bg = 'white', fg = 'firebrick')
emaillabel.grid(row=1, column=0, sticky='w', padx=10, pady= (8,0))


emailEntry = Entry(frame, width= 30, font = ('Arial',13))
emailEntry.grid(row=2, column=0, pady= (8,0))

usernamelabel = Label(frame, text = 'Username', font = ('Arial',10), bg = 'white', fg = 'firebrick')
usernamelabel.grid(row=3, column=0, sticky='w', padx=10, pady= (8,0))


usernameEntry = Entry(frame, width= 30, font = ('Arial',13))
usernameEntry.grid(row=4, column=0, pady= (8,0))

passwordlabel = Label(frame, text = 'Password', font = ('Arial',10), bg = 'white', fg = 'firebrick')
passwordlabel.grid(row=5, column=0, sticky='w', padx=10, pady= (8,0))


passwordEntry = Entry(frame, width= 30, font = ('Arial',13))
passwordEntry.grid(row=6, column=0, pady= (8,0))


confirmpasswordlabel = Label(frame, text = 'Confirm Password', font = ('Arial',10), bg = 'white', fg = 'firebrick')
confirmpasswordlabel.grid(row=7, column=0, sticky='w', padx=10, pady= (8,0))


confirmpasswordEntry = Entry(frame, width= 30, font = ('Arial',13))
confirmpasswordEntry.grid(row=8, column=0, pady= (8,0))


check = IntVar()
terms_and_contitions = Checkbutton(frame, text = 'I agree to the Terms & Conditions', font = ('Arial',9), cursor= 'hand2',
                                    variable= check)
terms_and_contitions.grid(row= 9, column= 0,padx=15, pady= (13,0))

signupButton = Button(frame, text = 'Signup', font = ('Arial',13, 'bold'),bd = 0, bg = 'red',fg = 'white'
                      , width=10, command= connect_database)
signupButton.grid(row=10, column=0,padx=15, pady= (13,0))


already_account_label = Label(frame, text = 'Already have an account?', font = ('Arial',10), bg = 'white', fg = 'firebrick')
already_account_label.grid(row=11, column=0, sticky='w', padx=15, pady= (50,0))


loginButton = Button(frame, text = 'Log In', font = ('Arial',7, 'bold underline'),bd = 0, bg = 'white',fg = 'blue', cursor= 'hand2',
                     command=login_page)
loginButton.place(x=180, y = 441)





signup_window.mainloop()



