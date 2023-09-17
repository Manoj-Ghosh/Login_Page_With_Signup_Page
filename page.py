from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql



welcome_window = Toplevel()
welcome_window.title('Welcome')

welcome_Image1 = ImageTk.PhotoImage(file ='welcome.jpg')
welcome_Label1 = Label(welcome_window, image= welcome_Image1)
welcome_Label1.grid()


Welcome_heading1 = Label(welcome_window, text = 'Welcome', font = ('Arial',10)
                    , bg = 'white', fg = 'red', background= 'white')
Welcome_heading1.place(x = 210, y =280)


