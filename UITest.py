#Tkinter libraries
import tkinter
from tkinter import *
from tkinter import ttk
#Matplot/graphing libraries
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
#Misc libraries
from collections import Counter 
import yfinance as yf
from yahoo_fin.stock_info import *
from tkinter import messagebox as mb


buyMoney = 10000.0
stockMoney=0.0
totalMoney=buyMoney


invested_before = {"AAPL":384.77,"TSLA":1627.63,"NFLX":410.34,"INTL":398.93,"GOOGL":1453}  #The day before? depends... you choose what data to put
shares = {"AAPL":1,"TSLA":3,"NFLX":2,"INTL":1,"GOOGL":5}
prices = {"AAPL":get_live_price('aapl'),"TSLA":get_live_price('tsla'),"NFLX":get_live_price('nflx'),"INTL":get_live_price('intl'),"GOOGL":get_live_price('googl')}
names = {"AAPL":"Apple Inc.","TSLA":"Tesla Inc.","NFLX":"Netflix Inc.","INTL":"Intel Inc.","GOOGL":"Google"}   #Put the names you want to show here
wlist = ["AAPL","TSLA","NFLX","INTL","GOOGL"]#current watchlist
    
root = tkinter.Tk()
root.title("Investment Simulator")
root.geometry('1280x700')
root.configure(bg='black')
home = Frame(root,width=1280, height=700)
watchlist = Frame(root,width=1280, height=700)
market = Frame(root,width=1280, height=700)
portfolio = Frame(root,width=1280, height=700)
graphing = Frame(root,width=1280, height=700)
search = Frame(root,width=1280, height=700)
global wlist_index
wlist_index = 0
def raise_frame(frame):
    frame.tkraise() #Brings desired frame to the top

for frame in (home, watchlist, market, portfolio, graphing, search):
    #Set frame to fill page
    frame.configure(bg="black") #Background Color
    frame.grid(row=0,column=0,sticky="nsew")
    #Page Buttons
    Button(frame, text='Home',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).place(x=50,y=50)
    Button(frame, text='Market',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).place(x=104,y=50)    
    Button(frame, text='Portfolio',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(portfolio)).place(x=160,y=50)
    Button(frame, text='Search',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(search)).place(x=225,y=50)
    
def buyStock(name):
    global stockMoney
    global buyMoney
    global totalMoney
    global numField
    global balance
    global cur_bal_txt
    stockPrice = get_live_price(name)#get the stock price of the wanted stock
    transaction = buyMoney - stockPrice*int(numField.get())#makes the transaction
    if transaction <0:
        mb.showerror("Error", "you do not have enough money for this purchase")
        return()
    buyMoney=transaction
    if str(name.upper()) in invested_before.keys():#updates the amount of shares and the price of it
        shares[name.upper()] += float(numField.get())
        prices[name.upper()] = stockPrice
        
    else:
        shares[name.upper()] = numField.get() #stores the # of shares you bought
        invested_before[name.upper()] = get_live_price(name) #stores the price you bought it at
        prices[name.upper()] = get_live_price(name) #stores the live price
        stock = yf.Ticker(name) 
        names[name.upper()] = stock.info['shortName'] #stores the actual company name
    stockMoney += stockPrice*float(numField.get()) #updates how much money in stocks you have
    balance = buyMoney #updates the balance in the UI
    cur_bal_txt1.configure(text="$"+str(balance))
    return()

def sellStock(name): #this function allows the user to sell stocks
    global buyMoney
    global stockMoney
    global totalMoney
    if(name.upper() not in shares.keys()): # if you don't have enough stocks to sell show a popup error
        mb.showerror("Error", "you do not own any of this stock")
        return()
    elif(int(numField.get())>shares[name]):
        mb.showerror("Error", "you do not have enough stocks for this transaction")
        return()
    stockPrice = get_live_price(name)#get the live price of a stock
    prices[name] = stockPrice #update stock price
    buyMoney = buyMoney+stockPrice #updates how much spending money you have
    if shares[name] == 1:#updates the stock count/portfolio
        shares.pop(name.upper(),None)
        invested_before.pop(name.upper(),None)
        prices.pop(name.upper(),None)
        names.pop(name.upper(),None)
    else:
        shares[name]-=1
    stockMoney-=stockPrice
    balance = buyMoney #updates the balance in the UI
    cur_bal_txt1.configure(text="$"+str(balance))
    return()

def updateMoney():
    global bal_stocks
    global totalMoney
    global bal_stocks_txt
    totalMoney = 0 
    for key in shares: #counts how much money you have in stocks
        prices[key] = get_live_price(key)
        totalMoney+=float(prices[key])*float(shares[key])
    totalMoney+=buyMoney #adds on the amount you have to spend
    if totalMoney!=bal_stocks: #if the newly calculated total money is not equal to the old amount, update it in UI
        bal_stocks = totalMoney
        bal_stocks_txt1.config(text="$"+str(bal_stocks))
    bal_stocks_txt1.after(10000,updateMoney)

def updateStocks():
    global buttons
    global wlist
    global names
    index = 0
    print("OWO")
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            try:
                buttons[i][j].config(text=(wlist[index]+"\n$"+
                                    str(round(get_live_price(wlist[index]),2)) + " x "  +
                                    str(shares[wlist[index]])+'\n' +
                                    str(round(get_live_price(wlist[index])
                                    - invested_before[wlist[index]],2)) +
                                    ' (' +str(round(get_live_price(wlist[index])/
                                    invested_before[wlist[index]],2))+
                                    '%)' + "\n" + names[wlist[index]]))
                index+=1
            except:
                break
    buttons[i][j].after(10000,updateStocks)
    return()
def watchlist_page(name):   #EDIT GRAPH HERE 
    raise_frame(graphing)#Keep this here
    #Edit everything after this line  (make sure the frame name is graphing, not root/master/self/frame .....)
    x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])

    fig = Figure(figsize=(3,3))#increase to make plot bigger
    a = fig.add_subplot(111)#scale??? bigger the number, the smaller the size
    a.scatter(y,x,color='red')
    
    a.set_title ("Estimation Grid", fontsize=16)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)

    canvas = FigureCanvasTkAgg(fig, master=graphing)
    canvas.get_tk_widget().place(x=100,y=100)
    canvas.draw()
    buyButton= Button(graphing, width=21,text="BUY",command=lambda:buyStock(name))
    buyButton.place(x=500,y=300)
    sellButton=Button(graphing, width=21,text="SELL",command=lambda:sellStock(name))
    sellButton.place(x=650,y=300)
    numField.place(x=500,y=330)
    graphing.mainloop()

if True:#Home Page
        #Balance
    balance = buyMoney
    cur_bal_txt = tkinter.Label(home, height = 1, bg = 'black', fg = 'grey', relief=FLAT)
    cur_bal_txt.configure(font=("Calibri", 30, ""))
    cur_bal_txt.configure(text="Your Balance:")
    cur_bal_txt1 = tkinter.Label(home,height = 1,bg='black',fg='white',font=("Calibri", 40, "bold"),text="$"+str(balance))
    cur_bal_txt.place(x=100,y=100)
    cur_bal_txt1.place(x=100,y=150)

        #Balance with stocks
    bal_stocks = totalMoney
    bal_stocks_txt = tkinter.Label(home, bg = 'black', fg = 'grey', relief=FLAT)
    bal_stocks_txt.configure(font=("Calibri", 30, ""))
    bal_stocks_txt.config(text="With Stocks:")
    bal_stocks_txt1 = Label(home,height=1, bg='black',fg ='white',font=("Calibri", 40, "bold"),text="$"+str(bal_stocks))
    bal_stocks_txt.place(x=500,y=100)
    bal_stocks_txt1.place(x=500,y=150)
    updateMoney()
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

def updateHomeList():
    global scroll_y
    global highest
    global prices
    global invested_before
    global names
    scroll_y.destroy()
    scroll_y = tkinter.Scrollbar(home, orient="vertical")
    scroll_y.configure(bg='black')
    for set in highest:
        Button(scroll_y, bg="white", relief=FLAT, command=lambda set=set:watchlist_page(set[0]),text = (set[0]+"\n$"+str(round(get_live_price(set[0]),2)) +"   "  + str(round(set[1] - invested_before[set[0]],2)) + "\n" + names[set[0]])).pack(side='right',expand=True)
    scroll_y.configure()
    scroll_y.place(relx=0.485, y=330, anchor=CENTER)
    scroll_y.after(10000,updateHomeList)
    return()
if True:
        #Watchlist(Home)
    watchlist_txt = tkinter.Text(home, height = 1, width = len("Priority Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
    watchlist_txt.configure(font=("Calibri", 30, ""))
    watchlist_txt.insert(tkinter.END, "Priority Watchlist:")
    watchlist_txt.place(relx=0.5, y=250, anchor=CENTER)
    watchlist_txt.config(state=DISABLED)
    k = Counter(shares) 
    highest = k.most_common(3) # Finding 3 highest values 
    x_coor=0
    scroll_y = tkinter.Scrollbar(home, orient="vertical")
    scroll_y.configure(bg='black')
    index = 0
    # Show price of stock, profit in %, how many shares
    for set in highest:
        Button(scroll_y, bg="white", relief=FLAT, command=lambda set=set:watchlist_page(set[0]),text = (set[0]+"\n$"+str(round(get_live_price(set[0]),2)) +"   "  + str(round(set[1] - invested_before[set[0]],2)) + "\n" + names[set[0]])).pack(side='right',expand=True)
    scroll_y.configure()
    scroll_y.place(relx=0.485, y=330, anchor=CENTER)
    updateHomeList()
    
        #Edit
    more = tkinter.Button(home, text="View All",relief=FLAT, width = 6, command = lambda:raise_frame(watchlist))
    more.place(relx=0.485, y=285, anchor = CENTER)

if True:#Watchlist
    wlist_txt = tkinter.Text(watchlist, height = 1, width = len("Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
    wlist_txt.configure(font=("Calibri", 30, ""))
    wlist_txt.insert(tkinter.END, "Watchlist:")
    wlist_txt.place(x=100,y=100)
    wlist_txt.config(state=DISABLED)

    numField = Entry(graphing, width=50)
    frame_canvas = Frame(watchlist)# Create a frame for the canvas with non-zero row&column weights
    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')#plot grid
    frame_canvas.grid_rowconfigure(0, weight=1)#set size
    frame_canvas.grid_columnconfigure(0, weight=1)
    frame_canvas.grid_propagate(False)# Set grid_propagate to False to allow 5-by-5 buttons resizing later
    canvas = Canvas(frame_canvas, bg="white")# Add a canvas in that frame
    canvas.grid(row=0, column=0, sticky="news")#"news" means north,east,west,south  ... covers the entire canvas
    vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)# Link a scrollbar to the canvas
    vsb.grid(row=0, column=1, sticky='ns')#covers from top to bottom (the scroll bar)
    canvas.configure(yscrollcommand=vsb.set)#link scrollbar to canvas
    frame_buttons = Frame(canvas, bg="white")# Create a frame to contain the buttons
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
    rows = 10# Add buttons to the frame
    columns = 10
    index=0
    buttons = [[Button() for j in range(columns)] for i in range(rows)]#creating the empty slots
    for i in range(0, rows):
        for j in range(0, columns):
            try:
                    #name, ticker
                    #share price x amount of shares
                    #profit amount profit %
                #filling the slots in
                buttons[i][j] = Button(frame_buttons, bg='white',
                                       relief=FLAT,
                                       command=lambda index=index:watchlist_page(wlist[index]),
                                       text=(wlist[index]+"\n$"+
                                             str(round(prices[wlist[index]],2)) + " x "  +
                                             str(shares[wlist[index]])+'\n' +
                                             str(round(get_live_price(wlist[index])
                                                              - invested_before[wlist[index]],2)) +
                                             ' (' +str(round(get_live_price(wlist[index])/
                                                             invested_before[wlist[index]],2))+
                                             '%)' + "\n" + names[wlist[index]]))
                buttons[i][j].grid(row=i, column=j, sticky='news')
                index += 1
            except:
                #once the index is invalid/wlist is out of items, break loop because all slots are filled
                break
            
    frame_buttons.update_idletasks()# Update buttons frames idle tasks to let tkinter calculate buttons sizes
    first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, columns)])# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
    first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, rows)])
    frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                        height=first5rows_height)
    canvas.config(scrollregion=canvas.bbox("all"))# Set the canvas scrolling region
    frame_canvas.place(x=100,y=150)#plot
    updateStocks()
    
#Market Page
graph = tkinter.Text(market, bg = 'black', fg = 'grey', relief=FLAT,height=1)
graph.configure(font=("Calibri", 30, ""))
graph.insert(tkinter.END, "How do i graph")
graph.place(x=100,y=400)
graph.config(state=DISABLED)

equity = 0
def updatePortfolio():
    global equity
    currentPrice =0
    for key in prices:
        prices[key]=get_live_price(key)
        currentPrice+=float(prices[key])*float(shares[key])
    if currentPrice!=equity:
        equity = currentPrice
        
    
#Portfolio Page
for key in prices:
    prices[key]=get_live_price(key)
    equity+=float(prices[key])*float(shares[key])
equity_txt = tkinter.Text(portfolio, height=2, bg = 'black', fg = 'grey', relief=FLAT)
equity_txt.configure(font=("Calibri", 30, ""))
equity_txt.insert(tkinter.END, "Your Equity:\n")
equity_txt.insert(tkinter.END, str(equity))
equity_txt.place(x=100,y=100)
equity_txt.config(state=DISABLED)


#Search Page
edit = Entry(search)
edit.place(relx=0.5,y=50)
edit.focus_set()
butt = Button(search, text='Find')
butt.place(relx=0.4,y=50)
def find():
    query = edit.get()
    returnData = pd.read_csv("https://ticker-2e1ica8b9.now.sh/keyword/"+query)
    print(returnData)
butt.config(command=find)

#Launch Porgram
home.tkraise()
root.mainloop()
