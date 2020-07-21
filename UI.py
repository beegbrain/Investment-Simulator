import tkinter
from tkinter import *
import numpy

root = tkinter.Tk()
root.title("Investment Simulator")
root.geometry('1000x1080')
root.configure(bg='black')
home = Frame(root,height=500)
market = Frame(root)
portfolio = Frame(root)

def raise_frame(frame):
    frame.tkraise()
    
for frame in (home, market, portfolio):
    frame.grid(row=0,column=0)   
    
#Home
cur_bal_txt = tkinter.Text(home, bg = 'black', fg = 'grey', relief=FLAT,height=1)
cur_bal_txt.configure(font=("Calibri", 30, ""))
cur_bal_txt.insert(tkinter.END, "Your Balance:")
cur_bal_txt.grid(row=1,column=1)
cur_bal_txt.config(state=DISABLED)
 
#Market
graph = tkinter.Text(market, bg = 'black', fg = 'grey', relief=FLAT,height=1)
graph.configure(font=("Calibri", 30, ""))
graph.insert(tkinter.END, "How do i graph")
graph.grid(row=1,column=1)
graph.config(state=DISABLED)

#Portfolio 
equity = "100,000,000"
equity_txt = tkinter.Text(portfolio, height=2, bg = 'black', fg = 'grey', relief=FLAT)
equity_txt.configure(font=("Calibri", 30, ""))
equity_txt.insert(tkinter.END, "Your Equity:\n")
equity_txt.insert(tkinter.END, "100,000,000")
equity_txt.grid(row = 1,column=1)
equity_txt.config(state=DISABLED)

#Switch Pages
Button(home, text='Home',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).grid(row=0,column=0,pady=20,padx=10)
Button(home, text='Market',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).grid(row=1,column=0,pady=20)
Button(home, text='Portfolio',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(portfolio)).grid(row=2,column=0,pady=20)

Button(market, text='Home', fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).grid(row=0,column=0,pady=20,padx=10)
Button(market, text='Market', fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).grid(row=1,column=0,pady=20)
Button(market, text='Portfolio', fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(portfolio)).grid(row=2,column=0,pady=20)

Button(portfolio, text='Home', fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).grid(row=0,column=0,pady=20,padx=10)
Button(portfolio, text='Market', fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).grid(row=1,column=0,pady=20)
Button(portfolio, text='Portfolio', fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(portfolio)).grid(row=2,column=0,pady=20)

home.configure(bg="black")
market.configure(bg="black")
portfolio.configure(bg="black")
home.tkraise()
root.mainloop()
