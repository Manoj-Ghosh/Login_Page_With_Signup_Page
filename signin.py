from tkinter import *
from PIL import ImageTk


# Functionality Part

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





login_window.mainloop()