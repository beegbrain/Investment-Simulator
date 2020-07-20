import tkinter
from tkinter import *
import numpy

app = tkinter.Tk()
app.title("Investment Simulator")
app.geometry('1920x1080')
app.configure(bg='black')


T = tkinter.Text(app, height=1, width=5, bg = 'black', fg = 'white', relief=FLAT)
T.place(x=10,y=30)
T.configure(font=("Calibri", 12, ""))
T.insert(tkinter.END, "Hello")
    
app.mainloop()
