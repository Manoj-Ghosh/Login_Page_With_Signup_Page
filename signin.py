from tkinter import *
from PIL import ImageTk

root = Tk()
root.geometry('990x660+50+50')

bgImage = ImageTk.PhotoImage(file = 'bg.jpg')

bgLabel = Label(root, image= bgImage)

#bgLabel.grid(row = 0, column = 0)
bgLabel.place(x=0, y=0)
#bgLabel.pack()

heading = Label(root, text = 'USER LOGIN')
heading.place(x = 650, y = 120)

root.mainloop()