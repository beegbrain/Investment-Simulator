import random
import tkinter as tk
import time as t
from yahoo_fin.stock_info import *
import yfinance as yf
import tkinter.font

buyMoney = 10000.0
stockMoney=0
totalMoney = buyMoney
stocks={}

def buyStock():#this function allows the user to buy stocks
    global buyMoney
    global stockMoney
    global totalMoney
    stockPrice = get_live_price(nameField.get())#get the stock price of the wanted stock
    buyMoney = buyMoney - stockPrice*int(numField.get())#makes the transaction
    if str(nameField.get()) in stocks.keys():#stores it in a dictionary
        stocks[nameField.get()][0] +=float(numField.get())
        stocks[nameField.get()][1] =stockPrice
        position = stocks[nameField.get()][2]
        newList.delete(position)#updates the list of stocks
        newList.insert(position, nameField.get()+"\n"+
                       str(stocks[nameField.get()]))
        
    else:
        stocks[nameField.get()] = [float(numField.get()),stockPrice,len(stocks)]
        newList.insert(len(stocks), nameField.get()+"\n"+
                       str(stocks[nameField.get()][:2]))
    stockMoney += stockPrice*float(numField.get())

    moneyLeft.config(text="Money to Spend: " + str(buyMoney))
    return()

def sellStock(): #this function allows the user to sell stocks
    global buyMoney
    global stockMoney
    global totalMoney
    stockPrice = get_live_price(nameField.get())#get the live price of a stock
    stocks[nameField.get()][1] = stockPrice #update stock price
    buyMoney = buyMoney+stockPrice #updates how much spending money you have
    if stocks[nameField.get()][0] == 1:#updates the stock count/portfolio
        stocks.pop(nameField.get(),None)
    else:
        stocks[nameField.get()][0]-=1
    stockMoney-=stockPrice
    moneyLeft.config(text="Money to Spend: " + str(buyMoney))
    return()

def updateMoney():#updates how much money you have total every 10s
    global totalMoney
    newMoney= 0
    for key, value in stocks.items():#recalculates the total money you have
        value[1] = float(get_live_price(key))
        newMoney+= value[0]*value[1]
    newMoney+=buyMoney
    if newMoney!=totalMoney:#if the newly calculated total money is not equal to the old amount, update it in UI
        totalMoney=newMoney
        textMoney.config(text="Total Money: "+ str(newMoney))
    textMoney.after(10000,updateMoney)
    return()

def updateStocks():#updates how much each stock costs every 10s
    print('es')
    for key, value in stocks.items():#goes through each ticker and checks if the price has changed every 10s
        if value[1] != get_live_price(key):
            value[1] = get_live_price(key)
            newList.delete(value[2])
            newList.insert(value[2], key+"\n"+
                       str(stocks[key]))
    newList.after(10000,updateStocks)
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
numField = tk.Entry(root, width=50)
numField.pack()
textMoney = tk.Label(root, text="Total Money: " + str(totalMoney))
textMoney.pack()
updateMoney()
moneyLeft = tk.Label(root, text="Money to Spend: " + str(buyMoney))
moneyLeft.pack()
newList = tk.Listbox(root)
newList.pack()
updateStocks()
root.mainloop()
