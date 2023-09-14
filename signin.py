from tkinter import *
from PIL import ImageTk


# Functionality Part








# GUI Part

root = Tk()
root.geometry('990x660+50+50')
root.resizable(0,0) # disabling the window size
root.title('Login Page') #adding title of the page



bgImage = ImageTk.PhotoImage(file = 'bg.jpg')

bgLabel = Label(root, image= bgImage)

#bgLabel.grid(row = 0, column = 0)
bgLabel.place(x=0, y=0)
#bgLabel.pack()

heading = Label(root, text = 'USER LOGIN', font = ('Arial',13,'bold')
                , bg = 'white', fg = 'firebrick')
heading.place(x = 650, y = 120)

usernameEntry = Entry(root, width = 23, font = ('Arial',11,'bold'),
                       bd = 0, fg = 'firebrick')
usernameEntry.place(x = 580, y = 200)
usernameEntry.insert(0, 'Username')

root.mainloop()