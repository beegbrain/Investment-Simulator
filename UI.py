import tkinter
from tkinter import *

app = tkinter.Tk()
app.title("Investment Simulator")
app.geometry('1920x1080')



T = tkinter.Text(app, height=1, width=5, bg = 'black', fg = 'white')
T.place(x=10,y=30)
T.configure(font=("Lucida Console", 12, ""))
T.insert(tkinter.END, "Hello")
    
app.mainloop()
