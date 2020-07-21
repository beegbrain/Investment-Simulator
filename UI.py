import tkinter

from tkinter import *
from tkinter import ttk
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
canvas = tkinter.Canvas(home)
def raise_frame(frame):
    frame.tkraise() #Brings desired frame to the top
    
for frame in (home, market, portfolio):
    #Set frame to fill page
    frame.configure(bg="black") #Background Color
>>>>>>> ef6a18437f8b4c09c2de9ccbac3404c6d3ec0e95
    frame.grid(sticky='nswe')
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=0,column=1)  

    #Page Buttons
    Button(frame, text='Home',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).place(x=50,y=50)
    Button(frame, text='Market',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).place(x=104,y=50)
    Button(frame, text='Portfolio',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(portfolio)).place(x=160,y=50)    
    

#Home Page
    #Balance
balance = 100000000
cur_bal_txt = tkinter.Text(home, height = 3, bg = 'black', fg = 'grey', relief=FLAT)
cur_bal_txt.configure(font=("Calibri", 30, ""))
cur_bal_txt.insert(tkinter.END, "Your Balance:\n")
cur_bal_txt.insert(tkinter.END, '$' + str(balance))
cur_bal_txt.tag_add("start", "2.0", "3.0")
cur_bal_txt.tag_config("start", background="black", foreground="white",font=("Calibri", 40, "bold"))
cur_bal_txt.place(x=100,y=100)
cur_bal_txt.config(state=DISABLED)

    #Balance with stocks
bal_stocks = 90000000
bal_stocks_txt = tkinter.Text(home, height = 3, bg = 'black', fg = 'grey', relief=FLAT)
bal_stocks_txt.configure(font=("Calibri", 30, ""))
bal_stocks_txt.insert(tkinter.END, "With Stocks: \n")
bal_stocks_txt.insert(tkinter.END, '$' + str(bal_stocks))
bal_stocks_txt.tag_add("start", "2.0", "3.0")
bal_stocks_txt.tag_config("start", background="black", foreground="white",font=("Calibri", 40, "bold"))
bal_stocks_txt.place(x=500,y=100)
bal_stocks_txt.config(state=DISABLED)
        #Bal Increase Today
inc_num = 500000
today = tkinter.Text(home, height = 3, width = len(str(inc_num)), bg = 'black', fg = 'grey', relief=FLAT)
today.configure(font=("Calibri", 30, ""))
today.insert(tkinter.END, "Today:\n")
today.insert(tkinter.END, ' +' + str(inc_num))
today.tag_add("start", "2.0", "3.0")
today.tag_config("start", background="#32CD32", foreground="white",font=("Calibri", 20, "bold"))
today.place(x=900,y=100)
today.config(state=DISABLED)
    #Watchlist
watchlist_txt = tkinter.Text(home, height = 1, width = len("Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
watchlist_txt.configure(font=("Calibri", 30, ""))
watchlist_txt.insert(tkinter.END, "Watchlist:")
watchlist_txt.place(relx=0.5, y=250, anchor=CENTER)
watchlist_txt.config(state=DISABLED)
invested_before = {"AAPL":384.77,"TSLA":1627.63,"NFLX":410.34,"INTL":398.93}  #The day before? depends... you choose what data to put
invested_curr = {"AAPL":390,"TSLA":1617,"NFLX":400,"INTL":405}   #Current invested profit
watchlist = [["AAPL","Apple Inc."],["TSLA","Tesla Inc."],["NFLX","Netflix Inc."],["INTL", "Intel Inc."]]   #Put the names you want to show here
scroll_y = tkinter.Scrollbar(home, orient="vertical")
scroll_y.configure(bg='black')
x_coor = 0
for index,i in enumerate(watchlist):
    text = i[0]+"\n$"+str(invested_curr[i[0]]) +"   "  + str(round(invested_curr[i[0]] - invested_before[i[0]],2)) + "\n" + i[1]
    button = tkinter.Button(scroll_y, text=text,font=("Helvectia", 9, ""),bg="white",relief=FLAT)
    button.place(x=x_coor)
    x_coor += len(str(invested_curr[i[0]]) +"   "  + str(round(invested_curr[i[0]] - invested_before[i[0]],2)))*6.75 + 2
scroll_y.configure(width=x_coor)
scroll_y.place(relx=0.485, y=330, anchor=CENTER)
    #Edit
edit = tkinter.Button(home, text="edit",relief=FLAT, width = 5, command = "send to watchlist edit")
edit.place(relx=0.485, y=285, anchor = CENTER)
>>>>>>> ef6a18437f8b4c09c2de9ccbac3404c6d3ec0e95


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


#Launch Porgram
home.tkraise()
root.mainloop()
