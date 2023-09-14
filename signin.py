from tkinter import *
from PIL import ImageTk


# Functionality Part

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
                   , cursor = 'hand2', font = ('Arial',11,'bold'), fg = 'green')
forgetButton.place(x = 710, y = 295)

loginButton = Button(login_window, text = 'Login', font = ('Open Sans',16,'bold')
                     , fg = 'white', bg = 'red', cursor= 'hand2', bd = 0, width = 19) #,activeforeground= 'white', activebackground= 'red'
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
                     , fg = 'blue', bg = 'white', cursor= 'hand2', bd = 0) #,activeforeground= 'white', activebackground= 'red'
newaccountButton.place(x = 727, y = 498)


login_window.mainloop()