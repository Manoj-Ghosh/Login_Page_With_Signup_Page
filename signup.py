from tkinter import *
from PIL import ImageTk



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
emaillabel.grid(row=1, column=0, sticky='w', padx=10)


emailEntry = Entry(frame, width= 30, font = ('Arial',13))
emailEntry.grid(row=2, column=0)

usernamelabel = Label(frame, text = 'Username', font = ('Arial',10), bg = 'white', fg = 'firebrick')
usernamelabel.grid(row=3, column=0, sticky='w', padx=10)


usernameEntry = Entry(frame, width= 30, font = ('Arial',13))
usernameEntry.grid(row=4, column=0)


signup_window.mainloop()



