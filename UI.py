import tkinter
from tkinter import *
import numpy

root = tkinter.Tk()
root.title("Investment Simulator")
root.geometry('1000x1080')
root.configure(bg='black')
frame = Frame(root)

def startup():
    frame.configure(bg='black')
    frame.pack()
    menubutton = Menubutton(frame, text= "≡")
    menubutton.menu = Menu(menubutton)
    menubutton["menu"]= menubutton.menu 
    menubutton.menu.add_command(label="Home", command=page_home)
    menubutton.menu.add_command(label="Portfolio", command=page_portfolio)
    menubutton.menu.add_command(label="Market", command=page_market)
    menubutton.grid(row=0,column=0,pady=20,padx=20)

def page_home():
    cur_bal_txt = tkinter.Text(frame, height=1, bg = 'black', fg = 'grey', relief=FLAT)
    cur_bal_txt.configure(font=("Calibri", 30, ""))
    cur_bal_txt.insert(tkinter.END, "Your Balance:")
    cur_bal_txt.grid(row=1,column=1)
    frame.grid_forget()
    return([cur_bal_txt])
def page_portfolio():
    equity = "100,000,000"
    for widget in page_home()[1:]:
        print(widget)
        widget.destroy()
    frame.grid_forget()
    equity_txt = tkinter.Text(frame, height=1, bg = 'black', fg = 'grey', relief=FLAT)
    equity_txt.configure(font=("Calibri", 30, ""))
    equity_txt.insert(tkinter.END, "Your Equity:")
    
    equity = tkinter.Text(frame, height=1, bg = 'black', fg = 'white', relief=FLAT)
    equity.configure(font=("Calibri", 50, ""))
    equity_txt.insert(tkinter.END, "100,000,000")
    
    equity_txt.grid(row=1,column=1)
    equity.grid(row=2,column=1)
    
def page_market():
    pass

startup()
page_home()

root.mainloop()


