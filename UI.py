import tkinter
from tkinter import *
import numpy

root = tkinter.Tk()
root.title("Investment Simulator")
root.geometry('1000x1080')
root.configure(bg='black')
home = Frame(root)
market = Frame(root)
portfolio = Frame(root)

def raise_frame(frame):
    frame.tkraise()

for frame in (home, market, portfolio):
    frame.grid(row=0, column=0, sticky='news')

#Switch Pages
Button(home, text='Home',fg='white', bg='black',command=lambda:raise_frame(home)).pack(side='left')
Button(home, text='Market',fg='white', bg='black', command=lambda:raise_frame(market)).pack()
Button(home, text='Portfolio',fg='white', bg='black', command=lambda:raise_frame(portfolio)).pack(side='right')

Button(market, text='Home', fg='white', bg='black',command=lambda:raise_frame(home)).pack()
Button(market, text='Market', fg='white', bg='black',command=lambda:raise_frame(market)).pack()
Button(market, text='Portfolio', fg='white', bg='black',command=lambda:raise_frame(portfolio)).pack()

Button(portfolio, text='Home', fg='white', bg='black',command=lambda:raise_frame(home)).pack()
Button(portfolio, text='Market', fg='white', bg='black',command=lambda:raise_frame(market)).pack()
Button(portfolio, text='Portfolio', fg='white', bg='black',command=lambda:raise_frame(portfolio)).pack()

#Home
cur_bal_txt = tkinter.Text(home, bg = 'white', fg = 'grey', relief=FLAT)
cur_bal_txt.configure(font=("Calibri", 30, ""))
cur_bal_txt.insert(tkinter.END, "Your Balance:")
cur_bal_txt.pack()
cur_bal_txt.config(state=DISABLED)
 
#Portfolio 
equity = "100,000,000"
equity_txt = tkinter.Text(portfolio, height=1, bg = 'black', fg = 'grey', relief=FLAT)
equity_txt.configure(font=("Calibri", 30, ""))
equity_txt.insert(tkinter.END, "Your Equity:")
equity_txt.insert(tkinter.END, "100,000,000")

equity_txt.place()

raise_frame(home)
root.mainloop()
