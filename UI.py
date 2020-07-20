import tkinter
from tkinter import *
import numpy

app = tkinter.Tk()
app.title("Investment Simulator")
app.geometry('1920x1080')
app.configure(bg='black')

menubutton = Menubutton(app, text= "≡")
menubutton.menu = Menu(menubutton)   
menubutton["menu"]= menubutton.menu 
  
text = tkinter.Text(app, height=1, width=5, bg = 'black', fg = 'white', relief=FLAT)
text.configure(font=("Calibri", 12, ""))
text.insert(tkinter.END, "Hello")

text.place(x=10,y=60)
menubutton.place(x=10,y=30)
app.mainloop()
