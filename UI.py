import tkinter
from tkinter import *
import numpy
global page
def switch_home():
    cur_bal_txt .destroy()
    text = tkinter.Text(app, height=1, bg = 'black', fg = 'grey', relief=FLAT)
    text.configure(font=("Calibri", 30, ""))
    text.insert(tkinter.END, "Dunno")
    text.grid(row=1,column=1)
    print("pog")
def switch_portfolio():
    global page
    page = "Portfolio"
def switch_market():
    global page
    page = "Market"

app = tkinter.Tk()
app.title("Investment Simulator")
app.geometry('1000x1080')
app.configure(bg='black')

menubutton = Menubutton(app, text= "≡")
menubutton.grid()
menubutton.menu = Menu(menubutton)
menubutton["menu"]= menubutton.menu 
menubutton.menu.add_command(label="Home", command=switch_home)
menubutton.menu.add_command(label="Portfolio", command=switch_portfolio)
menubutton.menu.add_command(label="Market", command=switch_market)

cur_bal_txt = tkinter.Text(app, height=1, bg = 'black', fg = 'grey', relief=FLAT)
cur_bal_txt.configure(font=("Calibri", 30, ""))
cur_bal_txt.insert(tkinter.END, "Your Balance:")

menubutton.grid(row=0,column=0)
cur_bal_txt.grid(row=1,column=1)
app.mainloop()


