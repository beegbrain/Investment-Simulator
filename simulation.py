import random
import tkinter as tk
import time as t
from yahoo_fin.stock_info import *
import yfinance as yf

keepGoing = True
buyMoney = 10000
stockMoney=0
totalMoney = buyMoney
stocks={}

def buyStock():#this function allows the user to buy stocks
    global buyMoney
    global stockMoney
    global totalMoney
    stockPrice = get_live_price(nameField.get())#get the stock price of the wanted stock
    buyMoney = buyMoney -stockPrice#makes the transaction
    if str(nameField.get()) in stocks.keys():#stores it in a dictionary
        stocks[nameField.get()][0] +=1
        stocks[nameField.get()][1] =stockPrice
    else:
        stocks[nameField.get()] = [1,stockPrice]
    stockMoney += stockPrice
    for key, value in stocks.items():
        totalMoney+= value[0]*value[1]
    totalMoney+=buyMoney

    return()

def sellStock():
    global buyMoney
    global stockMoney
    global totalMoney
    stockPrice = get_live_price(nameField.get())
    stocks[nameField.get()][1] = stockPrice
    buyMoney = buyMoney+stockPrice
    if stocks[nameField.get()][0] == 1:
        stocks.pop(nameField.get(),None)
    else:
        stocks[nameField.get()][0]-=1
    stockMoney-=stockPrice
    for key, value in stocks.items():
        totalMoney+= value[0]*value[1]
    totalMoney+=buyMoney
    return()
root = tk.Tk()
root.geometry('500x500')
root.configure(bg='black')
frame = tk.Frame(root)
frame.pack()
buy=tk.Button(frame,text="BUY",fg="red",
                 activebackground='blue',
                 command=buyStock)
buy.pack(side=tk.LEFT)
sell=tk.Button(frame,text="SELL",fg="red",
               activebackground='red',
               command=sellStock)
sell.place(x=500,y=500)
sell.pack()
nameField= tk.Entry(root)
nameField.pack()
root.mainloop()
