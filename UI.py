import tkinter

from tkinter import *
import numpy

from tkinter import *
from tkmacosx import Button

import tkinter.font as font



root = tkinter.Tk()
root.title("Investment Simulator")
root.geometry('1280x700')
root.configure(bg='black')
home = Frame(root,width=1280, height=700)
market = Frame(root,width=1280, height=700)
portfolio = Frame(root,width=1280, height=700)
home.configure(bg = "white")
def raise_frame(frame):
    frame.tkraise()
    
for frame in (home, market, portfolio):
    frame.configure(bg="black")
    frame.grid(sticky='nswe')
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=0,column=1)  
    
    #Switch Pages
    Button(frame, text='Home',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).place(x=50,y=50)
    Button(frame, text='Market',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).place(x=104,y=50)
    Button(frame, text='Portfolio',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(portfolio)).place(x=160,y=50)    
    
#Home
cur_bal_txt = tkinter.Text(home, bg = 'black', fg = 'grey', relief=FLAT,height=1)
cur_bal_txt.configure(font=("Calibri", 30, ""))
cur_bal_txt.insert(tkinter.END, "Your Balance:")
cur_bal_txt.place(x=100,y=100)
cur_bal_txt.config(state=DISABLED)
 
#Market
graph = tkinter.Text(market, bg = 'black', fg = 'grey', relief=FLAT,height=1)
graph.configure(font=("Calibri", 30, ""))
graph.insert(tkinter.END, "How do i graph")
graph.place(x=100,y=100)
graph.config(state=DISABLED)

#Portfolio 
title_txt = tkinter.Text(portfolio, height=0, bg = 'black', fg = '#C7C7C7', relief=FLAT, borderwidth = 0, highlightthickness = 0, bd = 0)
title_txt.configure(font=("Helvetica Neue bold", 30, ""))
title_txt.insert(tkinter.END, "Portfolio value:\n")
title_txt.place(x=100,y=100)
title_txt.config(state=DISABLED)

equity = "100,000,000"
equity_txt = tkinter.Text(portfolio, height=0, bg = 'black', fg = 'white', relief=FLAT, borderwidth = 0, highlightthickness = 0, bd = 0)
equity_txt.configure(font=("Helvetica Neue bold", 70, ""))
equity_txt.insert(tkinter.END, equity)
equity_txt.place(x=100,y=140)
equity_txt.config(state=DISABLED)

differnce_txt = tkinter.Text(portfolio, height=0, bg = 'black', fg = '#C7C7C7', relief=FLAT, borderwidth = 0, highlightthickness = 0, bd = 0)
differnce_txt.configure(font=("Helvetica Neue bold", 30, ""))
differnce_txt.insert(tkinter.END, "Today:\n")
differnce_txt.place(x=600,y=100)
differnce_txt.config(state=DISABLED)

buttonFont = font.Font(size=25, family = "Helvetica Neue bold")
Button(frame, text='+25.43',fg='white', bg='#89E274', borderless=0, borderwidth = 0, highlightthickness = 0, bd = 0, width = 200, height = 55, font = buttonFont, activebackground = '#89E274', bordercolor = '#89E274').place(x=600,y=155)

equity = "Your stocks:"
equity_txt = tkinter.Text(portfolio, height=0, bg = 'black', fg = 'white', relief=FLAT, borderwidth = 0, highlightthickness = 0, bd = 0)
equity_txt.configure(font=("Helvetica Neue bold", 55, ""))
equity_txt.insert(tkinter.END, equity)
equity_txt.place(x=100,y=300)
equity_txt.config(state=DISABLED)


home.tkraise()
root.mainloop()
