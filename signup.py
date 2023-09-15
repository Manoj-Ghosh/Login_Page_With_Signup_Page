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
emaillabel.grid(row=1, column=0, sticky='w', padx=10, pady= (5,0))


emailEntry = Entry(frame, width= 30, font = ('Arial',13))
emailEntry.grid(row=2, column=0, pady= (5,0))

usernamelabel = Label(frame, text = 'Username', font = ('Arial',10), bg = 'white', fg = 'firebrick')
usernamelabel.grid(row=3, column=0, sticky='w', padx=10, pady= (5,0))


usernameEntry = Entry(frame, width= 30, font = ('Arial',13))
usernameEntry.grid(row=4, column=0, pady= (5,0))

passwordlabel = Label(frame, text = 'Password', font = ('Arial',10), bg = 'white', fg = 'firebrick')
passwordlabel.grid(row=5, column=0, sticky='w', padx=10, pady= (5,0))


passwordEntry = Entry(frame, width= 30, font = ('Arial',13))
passwordEntry.grid(row=6, column=0, pady= (5,0))


confirmpasswordlabel = Label(frame, text = 'Confirm Password', font = ('Arial',10), bg = 'white', fg = 'firebrick')
confirmpasswordlabel.grid(row=7, column=0, sticky='w', padx=10, pady= (5,0))


confirmpasswordEntry = Entry(frame, width= 30, font = ('Arial',13))
confirmpasswordEntry.grid(row=8, column=0, pady= (5,0))


terms_and_contitions = Checkbutton(frame, text = 'I agree to the Terms & Conditions', font = ('Arial',9), cursor= 'hand2')
terms_and_contitions.grid(row= 9, column= 0,pady= (5,0) )


signup_window.mainloop()



