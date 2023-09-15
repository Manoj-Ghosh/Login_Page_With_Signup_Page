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
                , bg = 'white', fg = 'firebrick')
heading.grid(row = 0, column=0, padx = 18, pady=10)

signup_window.mainloop()



