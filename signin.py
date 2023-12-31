from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql




# Functionality Part


def page():
    welcome_window = Toplevel()
    welcome_window.title('Welcome')

    welcome_Image1 = ImageTk.PhotoImage(file ='welcome.jpg')
    welcome_Label1 = Label(welcome_window, image= welcome_Image1)
    welcome_Label1.grid()


    Welcome_heading1 = Label(welcome_window, text = 'Welcome', font = ('Arial',10)
                    , bg = 'white', fg = 'magenta2', background= 'white')
    Welcome_heading1.place(x = 200, y =260)




def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    
    


def forget_pass():

    def change_password():
        if usernameEntryy.get() =='' or PasswordEntryy.get() =='' or ConPasswordEntryy.get() =='':
            messagebox.showerror('Error', 'All Fields Are Required', parent = window)

        elif PasswordEntryy.get() != ConPasswordEntryy.get():
            messagebox.showerror('Error', 'Password and Confirm Password are Not Matching', parent = window)

        else:
            con = pymysql.connect(host= 'localhost', user='root', password='1234', database= 'userdata')
            mycursor = con.cursor()

            query = 'select * from data where username = %s'
            mycursor.execute(query, (usernameEntryy.get()))
            roww = mycursor.fetchone()

            if roww == None:
                messagebox.showerror('Error', 'Incorrect Username', parent = window)

            else:

                query = 'update data set password =%s where username =%s'
                mycursor.execute(query, (PasswordEntryy.get(), usernameEntryy.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset. Please Login With The New Password', parent = window)
                window.destroy()
    

        



    window = Toplevel()
    window.title('Change Password')

    bgImage = ImageTk.PhotoImage(file = 'background.jpg')
    bgLabel = Label(window, image= bgImage)
    bgLabel.grid()


    heading = Label(window, text = 'RESET PASSWORD', font = ('Arial',18)
                , bg = 'white', fg = 'magenta2', background= 'white')
    heading.place(x = 488, y =60)

    usernamelabel = Label(window, text = 'Username', font = ('Arial',10,'bold'), bg = 'white', fg = 'magenta2')
    usernamelabel.place(x = 470, y = 130)

    usernameEntryy = Entry(window, width= 30, font = ('Arial',13))
    usernameEntryy.place(x = 470, y = 160)

    #Frame(window, width= 250, height= 2).place(x= 470, y=180)


    Passwordlabel = Label(window, text = 'New Password', font = ('Arial',10,'bold'), bg = 'white', fg = 'magenta2')
    Passwordlabel.place(x = 470, y = 190)

    PasswordEntryy = Entry(window, width= 30, font = ('Arial',13))
    PasswordEntryy.place(x = 470, y = 220)

    #Frame(window, width= 250, height= 2).place(x= 470, y=180)


    ConPasswordlabel = Label(window, text = 'Confirm New Password', font = ('Arial',10,'bold'), bg = 'white', fg = 'magenta2')
    ConPasswordlabel.place(x = 470, y = 250)

    ConPasswordEntryy = Entry(window, width= 30, font = ('Arial',13))
    ConPasswordEntryy.place(x = 470, y = 280)

    #Frame(window, width= 250, height= 2).place(x= 470, y=180)



    submitButton = Button(window, text = 'SUBMIT', font = ('Open Sans',16,'bold')
                     , fg = 'white', bg = 'magenta2', cursor= 'hand2', bd = 0, width = 19, command=change_password) #,activeforeground= 'white', activebackground= 'red'
    submitButton.place(x = 478, y = 340)






    window.mainloop()









def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:

            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()

        except:
            messagebox.showerror('Error', 'Connection is not established, try again')
            return
        
        query = 'use userdata'
        mycursor.execute(query)

        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome', 'Login is Successfull')
            import page
            clear()







    


def signup_page():
    login_window.destroy()
    import signup

def hide():
    Open_eye.config(file = 'closeye.png')
    passwordEntry.config(show= '*')
    eyeButton.config(command= show)

def show():
     Open_eye.config(file = 'openeye.png')
     passwordEntry.config(show= '')
     eyeButton.config(command= hide)



def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)










# GUI Part

login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0) # disabling the window size
login_window.title('Login Page') #adding title of the page



bgImage = ImageTk.PhotoImage(file = 'bg.jpg')

bgLabel = Label(login_window, image= bgImage)

#bgLabel.grid(row = 0, column = 0)
bgLabel.place(x=0, y=0)
#bgLabel.pack()

heading = Label(login_window, text = 'USER LOGIN', font = ('Arial',13,'bold')
                , bg = 'white', fg = 'firebrick')
heading.place(x = 650, y = 120)

usernameEntry = Entry(login_window, width = 23, font = ('Arial',11,'bold'),
                       bd = 0, fg = 'firebrick')
usernameEntry.place(x = 580, y = 200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width = 250, height= 2, bg = 'firebrick') # for creating line at the bottom of username
frame1.place(x = 580, y = 222) 

passwordEntry = Entry(login_window, width = 23, font = ('Arial',11,'bold'),
                       bd = 0, fg = 'firebrick')
passwordEntry.place(x = 580, y = 260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width = 250, height= 2, bg = 'firebrick') # for creating line at the bottom of password
frame2.place(x = 580, y = 282) 


Open_eye = PhotoImage(file = 'openeye.png')
eyeButton = Button(login_window, image= Open_eye, bd = 0, bg = 'white', activebackground= 'white'
                   , cursor = 'hand2', command= hide)
eyeButton.place(x = 800, y = 254)

forgetButton = Button(login_window, text = 'Forgot Password?', bd = 0, bg = 'white', activebackground= 'white'
                   , cursor = 'hand2', font = ('Arial',11,'bold'), fg = 'green', command=forget_pass)
forgetButton.place(x = 710, y = 295)

loginButton = Button(login_window, text = 'Login', font = ('Open Sans',16,'bold')
                     , fg = 'white', bg = 'red', cursor= 'hand2', bd = 0, width = 19, command = login_user) #,activeforeground= 'white', activebackground= 'red'
loginButton.place(x = 578, y = 350)


orLabel = Label(login_window, text = '---------- OR ----------', font = ('Arial',16,'italic'), fg= 'red', bg = 'white' )
orLabel.place(x = 613, y = 400)

facebook_logo = PhotoImage(file = 'facebook.png')
fbLabel = Label(login_window, image = facebook_logo, bg = 'white')
fbLabel.place(x = 640, y = 440)

twitter_logo = PhotoImage(file = 'twitter.png')
twitterLabel = Label(login_window, image = twitter_logo, bg = 'white')
twitterLabel.place(x = 690, y = 440)

google_logo = PhotoImage(file = 'google.png')
googleLabel = Label(login_window, image = google_logo, bg = 'white')
googleLabel.place(x = 740, y = 440)

signupLabel = Label(login_window, text = 'Dont have an account?', font = ('Arial',11,'italic'), fg= 'red', bg = 'white' )
signupLabel.place(x = 580, y = 500)

newaccountButton = Button(login_window, text = 'Create Account', font = ('Open Sans',11,'bold underline')
                     , fg = 'blue', bg = 'white', cursor= 'hand2', bd = 0, command= signup_page) #,activeforeground= 'white', activebackground= 'red'
newaccountButton.place(x = 727, y = 498)


login_window.mainloop()