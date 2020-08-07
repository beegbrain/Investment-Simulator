#Tkinter libraries
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
#Matplot/graphing libraries
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#Misc libraries
from collections import Counter 
import yfinance as yf
from yahoo_fin.stock_info import *
import os
from collections import OrderedDict
import time
import datetime

root = tkinter.Tk()
root.title("Investment Simulator")
root.geometry('1280x700')
root.configure(bg='black')
home = Frame(root,width=1280, height=700)
watchlist = Frame(root,width=1280, height=700)
market = Frame(root,width=1280, height=700)
portfolio = Frame(root,width=1280, height=700)
graphing = Frame(root,width=1280, height=700)
    
import os

#Grabbing Data

global visible
global cur_bal_txt1
datafile = open(os.path.dirname(os.path.abspath(__file__)) + "\data.txt").read().split()
wlist = eval(datafile[0])#current watchlist
plist = eval(datafile[1])
invested_before = eval(datafile[2])  #The day before? depends... you choose what data to put
shares = eval(datafile[3])
balance = 0.0
buyMoney = float(datafile[4])
prev_bal  = float(datafile[5])
stockMoney=0.0
equity = 0.0
totalMoney=buyMoney
bal_stocks = totalMoney
prices = dict()
names = dict()
for index in wlist:
    response = requests.get("https://ticker-2e1ica8b9.now.sh/keyword/"+index)
    data = response.text.split(':')
    names[index] = data[-1][1:-3]
    equity += get_live_price(index) * shares[index]




visible = '..'
wlist_index = 0

def listbox_list(query):
    name = list()
    if query != [] and query != '':
        response = requests.get("https://ticker-2e1ica8b9.now.sh/keyword/"+query)
        data = response.text.split(',')
        try:
            for index in range(0, len(data), 2):
                data[index] = data[index].split(':')
                name.append(data[index][1].replace('"',''))#Appends company name to this list  
        except:pass
    return name[:2]
def listbox_update(data):
    global entry
    data = listbox_list(entry.get())
    if data != []:
        print("updating search bar",entry.get())
        # delete previous data
        try:
            listbox.delete(0, 'end')
        except:pass
        # sorting data 
        data = sorted(data, key=str.lower)
        # put new data
        for item in data:
            listbox.insert('end', item)
def on_change(*args):
    global test_list
    value = var_text.get()
    value = value.strip().lower()
    data = []
    for item in test_list:
        if value in item.lower():
            data.append(item)    
    listbox_update(data)# update data in listbox
def on_select(event):
    try:
        graph_page(event.widget.get(event.widget.curselection()))
    except:pass
def buyStock(name):
    global stockMoney
    global buyMoney
    global totalMoney
    global numField
    global balance
    stockPrice = get_live_price(name)#get the stock price of the wanted stock
    transaction = buyMoney - stockPrice*int(numField.get())#makes the transaction
    if transaction <0:
        mb.showerror("Error", "you do not have enough money for this purchase")
        return()
    elif float(numField.get())<=0:
        mb.showerror("Error", "You cannot purchase a nonpositive amount of stocks")
        return()
    elif int(numField.get()) != float(numField.get()):
        mb.showerror("Error", "You cannot buy a noninteger amount of stocks")
        return()
    #elif datetime.datetime.now() > datetime.datetime.now().replace(hour=13,minute=30,second=0,microsecond=0):
        #mb.showerror("Error", "The stock market has closed for today! You cannot trade now")
        #return()
    buyMoney=transaction
    if str(name.upper()) in invested_before.keys():#updates the amount of shares and the price of it
        shares[name.upper()] += float(numField.get())
        prices[name.upper()] = stockPrice
        
    else:
        plist.append(name.upper())
        shares[name.upper()] = int(numField.get()) #stores the # of shares you bought
        invested_before[name.upper()] = get_live_price(name) #stores the price you bought it at
        prices[name.upper()] = get_live_price(name) #stores the live price
        stock = yf.Ticker(name) 
        names[name.upper()] = stock.info['shortName'] #stores the actual company name
    stockMoney += stockPrice*float(numField.get()) #updates how much money in stocks you have
    balance = buyMoney #updates the balance in the UI
    cur_bal_txt1.configure(text="$"+str(round(balance,2)))
    return()
def sellStock(name): #this function allows the user to sell stocks
    global buyMoney
    global stockMoney
    global totalMoney
    global bal_stocks
    if(name.upper() not in shares.keys()): # if you don't have enough stocks to sell show a popup error
        mb.showerror("Error", "you do not own any of this stock")
        return()
    elif(int(numField.get())>shares[name]):
        mb.showerror("Error", "you do not have enough stocks for this transaction")
        return()
    elif float(numField.get())<=0:
        mb.showerror("Error", "You cannot sell a nonpositive amount of stocks")
        return()
    elif int(numField.get()) != float(numField.get()):
        mb.showerror("Error", "You cannot sell a noninteger amount of stocks")
        return()
    #elif datetime.datetime.now() > datetime.datetime.now().replace(hour=13,minute=30,second=0,microsecond=0):
        #mb.showerror("Error", "The stock market has closed for today! You cannot trade now")
        #return()
    stockPrice = get_live_price(name)#get the live price of a stock
    prices[name] = stockPrice #update stock price
    buyMoney = buyMoney+stockPrice #updates how much spending money you have
    if shares[name] == 1:#updates the stock count/portfolio
        shares[name] = shares[names] - int(numField.get())
        if shares[name] == 0:
            del shares[name]
            del names[name]
            plist.remove(name)
        invested_before.pop(name.upper(),None)
        prices.pop(name.upper(),None)
        names.pop(name.upper(),None)
    else:
        shares[name]-=1
    stockMoney-=stockPrice
    balance = buyMoney #updates the balance in the UI
    cur_bal_txt1.configure(text="$"+str(round(balance,2)))
    return()
def updateMoney():
    print('updating money')
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
        bal_stocks_txt1.config(text="$"+str(round(bal_stocks,2)))
    print('successful')
    bal_stocks_txt1.after(20000,updateMoney)
def updatewStocks():
    print('updating stocks')
    global buttons
    global wlist
    global names
    index = 0
    if visible == 'watchlist':
        print('successful ')
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                #Formatting the button text
                try:
                    ticker = yf.Ticker(wlist[index])
                    buttons[i][j].config(text=(wlist[index]+"\n$"+
                                        str(round(get_live_price(wlist[index]),2)) +'\n' +
                                        str(round(get_live_price(wlist[index]) - int(ticker.history(period='1d')['Open']),2)) +
                                        ' (' +str(round(get_live_price(wlist[index])/int(ticker.history(period='1d')['Open']),2))+
                                        '%)' + "\n" + names[wlist[index]]))
                                        
                    index+=1
                except:pass
    buttons.after(20000,updatewStocks)#Updates it every 20,000 ms
    if visible != 'watchlist':print('suspended')#If not on the right page, stop updates 
def updatepStocks():
    print('updating stocks')
    global pbuttons
    global plist
    global names
    index = 0
    if visible == 'portfolio':
        print('successful portfolio')
        for i in range(len(pbuttons)):
            for j in range(len(pbuttons[i])):
                try:
                    ticker = yf.Ticker(plist[index])
                    pbuttons[i][j].config(text=(plist[index]+"\n$"+
                                        str(round(get_live_price([index]),2)) +'\n' +
                                        str(round(get_live_price(plist[index]) - int(ticker.history(period='1d')['Open']),2)) +
                                        ' (' +str(round(get_live_price(plist[index])/int(ticker.history(period='1d')['Open']),2))+
                                        '%)' + "\n" + names[plist[index]]))
                    index+=1
                except:pass
    pbuttons.after(20000,updatepStocks)
    if visible != 'portfolio':print('suspended')#If not on the right page, stop updates
def updateEquity():
    print('updating equity')
    global equity
    global wlist
    global equity_txt
    temp = 0
    for index in wlist:
        temp += get_live_price(wlist[index]) * shares[wlist[index]]
    if temp != equity:
        equity_txt.config(text='$'+str(round(equity,2)))
    print('succesful')
    equity_txt.after(25000,updateEquity)
def updateHomeList():
    print('updating home watchlist')
    global scroll_y
    global highest
    global prices
    global invested_before
    global names
    if visible == 'home':
        print('successful ')
        if len(wlist) > 0:
            scroll_y.destroy()
            scroll_y = tkinter.Scrollbar(home, orient="vertical")
            scroll_y.configure(bg='black')
            for set in highest:
                ticker = yf.Ticker(set[0])
                Button(scroll_y, bg="white", relief=FLAT, command=lambda set=set:graph_page(set[0]),text = (set[0]+"\n$"+str(round(get_live_price(set[0]),2)) 
                                                                                                        +"  "  + str(round(round(get_live_price(set[0]),2) - int(ticker.history(period='1d')['Open']),2))
                                                                                                        + "\n" + names[set[0]])).pack(side='right',expand=True)
            scroll_y.configure()
            scroll_y.place(relx=0.485, y=330, anchor=CENTER)
    else:
        print('suspended')
    scroll_y.after(20000,updateHomeList)
def startWatching(stock):
    global wlist
    print('added ' + stock.upper() + ' to watchlist')
    ticker = yf.Ticker(stock)
    wlist.append(stock.upper())
    names[stock.upper()]=ticker.info['shortName']
    shares[stock.upper()]=0
    return()
def stopWatching(stock):
    print('removed ' + stock.upper() + ' from watchlist')
    if stock in wlist:
        wlist.remove(stock)
        names.pop(stock.upper())
    return()
for frame in (watchlist, market, portfolio, graphing, home):
    #Set frame to fill page
    frame.configure(bg="black") #Background Color
    frame.grid(row=0,column=0,sticky="nsew")
    #Search bar
    if frame == home:  
        global test_list
        global entry
        test_list = ''
        var_text = StringVar()
        var_text.trace('w', on_change)
        entry = Entry(frame, textvariable=var_text)
        entry.place(relx=0.7,y=50)
        entry.bind('<KeyRelease>', on_change)
        listbox = Listbox(frame, height = 2)
        listbox.place(relx=0.7,y=65)
        listbox.bind('<<ListboxSelect>>', on_select)
        test_list = listbox_list(var_text.get())
        listbox_update(test_list)
    #Page Buttons
    Button(frame, text='Home',font=("Calibri", 25, ""),fg='black', bg='grey', relief=FLAT, command=lambda:raise_home()).place(x=50,y=20)
    Button(frame, text='Market',font=("Calibri", 25, ""),fg='black', bg='grey', relief=FLAT, command=lambda:raise_market()).place(x=180,y=20)    
    Button(frame, text='Portfolio',font=("Calibri", 25, ""),fg='black', bg='grey', relief=FLAT, command=lambda:raise_portfolio()).place(x=330,y=20)
  
def xlabel(x):
    if x==daytime:
        return "5 minutes"
    if x==weektime:
        return "1 hour"
    else:
        return "1 day"
def grapher(x,y,name):
    try:
        canvas.delete('all')
    except:
        pass
    fig = Figure(figsize=(5,5.5))#increase to make plot bigger
    fig.patch.set_facecolor('black')
    a = fig.add_subplot(111)#scale??? bigger the number, the smaller the size
    ticker = yf.Ticker(name.upper())
    a.plot(x,y,color='#98B7C3')
    a.set_facecolor('black')
    a.set_title ('', fontsize=13, color = "white")
    a.set_ylabel("", fontsize=14)
    a.set_xlabel(xlabel(x), fontsize=14)
    a.xaxis.label.set_color('white')
    a.tick_params(axis='x', colors='white')
    a.yaxis.label.set_color('white')
    a.tick_params(axis='y', colors='white')
    title = (name + "(" + yf.Ticker(name.upper()).info['longName'] + ")\n"
        + 'Current Price: $' + str(round(get_live_price(name.upper()),2))
        + '\nOpen: $' + str(round(int(ticker.history(period='1d')['Open']),2)))
    canvas = FigureCanvasTkAgg(fig, master=graphing)#Putting the plot onto a canvas
    title_txt = Text(graphing, height = 4, width = 56, bg = 'black', fg = 'white', relief=FLAT, font=("Serif", 13, ""))
    title_txt.tag_configure("center", justify='center')
    title_txt.insert("1.0", title)
    title_txt.tag_add("center", "1.0", "end")
    title_txt.tag_add("start", "1.0", "1.99")
    title_txt.tag_config("start", font=("Serif", 15, ""))
    title_txt.config(state=DISABLED)
    title_txt.place(x=1280/2,y=150)
    canvas.get_tk_widget().place(x=150,y=150)#Placing the canvas on window
    canvas.draw()


def graph_page(name):   #EDIT GRAPH HERE 
    visible = 'graphing'
    print('now GRAPHING')
    graphing.tkraise()#Keep this here
    #Edit everything after this line  (make sure the frame name is graphing, not root/master/self/frame .....)
    global weektime
    global yeartime
    global daytime
    global numField
    global cur_bal_txt1
    numField = Entry(graphing, width=50)
    nflx = yf.Ticker(name)
    nflx.info
    yearpricelist=list()
    for i in nflx.history(period="1y",interval="1d")["Close"]:#Inputs the corresponding lists into the plot
        yearpricelist.append(i)
    yearprice= np.array(yearpricelist)
    daypricelist=list()
    for i in nflx.history(period="1d",interval="5m")["Close"]:
        daypricelist.append(i)
    dayprice= np.array(daypricelist)
    weekpricelist=list()
    for i in nflx.history(period="5d",interval= "1h")["Close"]:
        weekpricelist.append(i)

    weekprice= np.array(weekpricelist)
    weektime=list(range(0,len(weekpricelist)))
    yeartime=list(range(0,len(yearpricelist)))
    daytime=list(range(0,len(daypricelist)))
    #Buttons for different times
    Button(graphing, text='Past day',fg='black', bg='grey', relief=FLAT, command=lambda:grapher(daytime,dayprice,name)).place(x=150,y=120)
    Button(graphing, text='Past 5 days',fg='black', bg='grey', relief=FLAT, command=lambda:grapher(weektime,weekprice,name)).place(x=210,y=120) 
    Button(graphing, text='Past year',fg='black', bg='grey', relief=FLAT, command=lambda:grapher(yeartime,yearprice,name)).place(x=285,y=120) 
    grapher(daytime,dayprice,name)#default graph
    buyButton= Button(graphing, width=21,text="BUY",command=lambda:buyStock(name))
    buyButton.place(x=750,y=300)
    sellButton=Button(graphing, width=21,text="SELL",command=lambda:sellStock(name))
    sellButton.place(x=900,y=300)
    numField.place(x=750,y=330)
    addWatchlist = Button(graphing,width=42, text="Add to Watchlist",command=lambda:startWatching(name))
    delWatchlist = Button(graphing,width=42, text="Remove from Watchlist",command=lambda:stopWatching(name))
    if name in wlist:
        delWatchlist.place(x = 750, y=250)
    else:addWatchlist.place(x = 750, y=250)
    graphing.mainloop()

def raise_home():
    global visible
    global cur_bal_txt1
    visible = 'home'
    print('now on HOME')
        #Balance
    home.tkraise()
    balance = buyMoney
    cur_bal_txt = tkinter.Label(home, height = 1, bg = 'black', fg = 'grey', relief=FLAT)
    cur_bal_txt.configure(font=("Calibri", 30, ""))
    cur_bal_txt.configure(text="Your Balance:")
    cur_bal_txt1 = tkinter.Label(home,height = 1,bg='black',fg='white',font=("Calibri", 40, "bold"),text="$"+str(round(balance,2)))
    cur_bal_txt.place(x=100,y=100)
    cur_bal_txt1.place(x=100,y=150)
        #Balance with stocks
    bal_stocks_txt = tkinter.Label(home, bg = 'black', fg = 'grey', relief=FLAT)
    bal_stocks_txt.configure(font=("Calibri", 30, ""))
    bal_stocks_txt.config(text="With Stocks:")
    global bal_stocks_txt1
    bal_stocks_txt1 = Label(home,height=1, bg='black',fg ='white',font=("Calibri", 40, "bold"),text="$"+str(round(bal_stocks,2)))
    bal_stocks_txt.place(x=500,y=100)
    bal_stocks_txt1.place(x=500,y=150)
    updateMoney()
            #Bal Increase Today
    inc_num = round(balance-prev_bal,2)
    today = tkinter.Text(home, height = 3, width = max([len(str(inc_num)),len('Today: ')]), bg = 'black', fg = 'grey', relief=FLAT)
    today.configure(font=("Calibri", 30, ""))
    today.insert(tkinter.END, "Today:\n")
    if (inc_num) >= 0:
        today.insert(tkinter.END, ' +' + str(inc_num))
        today.tag_add("start", "2.0", "3.0")
        today.tag_config("start", background="#32CD32", foreground="white",font=("Calibri", 20, "bold"))
    else:
        today.insert(tkinter.END, ' ' + str(inc_num))
        today.tag_add("start", "2.0", "3.0")
        today.tag_config("start", background="#FF0000", foreground="white",font=("Calibri", 20, "bold"))
    today.place(x=900,y=100)
    today.config(state=DISABLED)
    
    if True:
            #Watchlist(Home)
        watchlist_txt = tkinter.Text(home, height = 1, width = len("Priority Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
        watchlist_txt.configure(font=("Calibri", 30, ""))
        watchlist_txt.insert(tkinter.END, "Priority Watchlist:")
        watchlist_txt.place(relx=0.5, y=250, anchor=CENTER)
        watchlist_txt.config(state=DISABLED)
        empty = tkinter.Text(home, height = 10, width = len("Search up a stock and click add to watchlist"), bg = 'black', fg = 'white', relief=FLAT)
        empty.configure(font=("Calibri", 30, ""))
        empty.insert(tkinter.END, "Search up a stock and click add to watchlist")
        empty.config(state=DISABLED)
        k = Counter(shares) 
        global highest
        try:
            highest = k.most_common(3) # Finding 3 highest values 
        except:
            highest = k.most_common()
        x_coor=0   
        global scroll_y         
        scroll_y = tkinter.Scrollbar(home, orient="vertical")
        scroll_y.configure(bg='black')
        if len(wlist) > 0:
            empty.configure(fg = 'black')
            empty.place(relx=0.5, y=520, anchor=CENTER)
            index = 0
            # Show price of stock, profit in %, how many shares
            for set in highest:
                ticker = yf.Ticker(set[0])
                Button(scroll_y, bg="white", relief=FLAT, command=lambda set=set:graph_page(set[0]),text = (set[0]+"\n$"+str(round(get_live_price(set[0]),2)) 
                                                                                                        +"  "  + str(round(round(get_live_price(set[0]),2) - int(ticker.history(period='1d')['Open']),2))
                                                                                                        + "\n" + names[set[0]])).pack(side='right',expand=True)
            scroll_y.configure()
            scroll_y.place(relx=0.485, y=330, anchor=CENTER)
            
                #Edit
            more = tkinter.Button(home, text="View All",relief=FLAT, width = 6, command = lambda:raise_watchlist())
            more.place(relx=0.485, y=285, anchor = CENTER)
        else:
            #If watchlist is empty, display text
            empty.place(relx=0.5, y=520, anchor=CENTER)
            
            
        updateHomeList()
    

def raise_watchlist():
    global visible
    visible = 'watchlist'
    print('now on WATCHLIST')
    watchlist.tkraise()
    wlist_txt = tkinter.Text(watchlist, height = 1, width = len("Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
    wlist_txt.configure(font=("Calibri", 30, ""))
    wlist_txt.insert(tkinter.END, "Watchlist:")
    wlist_txt.place(x=100,y=100)
    wlist_txt.config(state=DISABLED)
    
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
    global buttons
    buttons = [[Button() for j in range(columns)] for i in range(rows)]#creating the empty slots
    for i in range(0, rows):
        for j in range(0, columns):
            try:
                #name, ticker
                #share price x amount of shares
                #profit amount profit %
                #filling the slots in
                ticker = yf.Ticker(wlist[index])
                buttons[i][j] = Button(frame_buttons, bg='white',
                                       relief=FLAT,
                                       command=lambda index=index:graph_page(wlist[index]),
                                       text=(wlist[index]+"\n$"+
                                            str(round(get_live_price(wlist[index]),2)) +'\n' +
                                            str(round(get_live_price(wlist[index]) - int(ticker.history(period='1d')['Open']),2)) +
                                            ' (' +str(round(get_live_price(wlist[index])/int(ticker.history(period='1d')['Open']),2))+
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
    updatewStocks()
   
def raise_market():
    global visible
    visible = 'market'
    print('now on MARKET')
    market.tkraise()
    def year(ticker):
        ticker = yf.Ticker(ticker)
        ticker.info
        yearpricelist=list()
        for f, b in zip(ticker.history(period="1y",interval="5d")["Open"], ticker.history(period="1y",interval="5d")["Close"]):
            yearpricelist.append( 100 * (b - f) / f)
        yearprice= np.array(yearpricelist)
        yeartime=list(range(0,len(yearpricelist)))
        return (yeartime,yearprice)
    
    def day(ticker):
        ticker = yf.Ticker(ticker)
        ticker.info
        daypricelist=list()
        for f, b in zip(ticker.history(period="1d",interval="5m")["Open"], ticker.history(period="1d",interval="5m")["Close"]):
            daypricelist.append( 100 * (int(b) - int(f)) / int(f))
        dayprice= np.array(daypricelist)
        daytime=list(range(0,len(daypricelist)))
        return (daytime,dayprice)

    def week(ticker):
        weekpricelist=list()
        ticker = yf.Ticker(ticker)
        ticker.info
        for f, b in zip(ticker.history(period="5d",interval= "1h")["Open"], ticker.history(period="5d",interval= "1h")["Close"]):
            weekpricelist.append( 100 * (b - f) / f)    
        weekprice= np.array(weekpricelist)
        weektime=list(range(0,len(weekpricelist)))
        return (weektime,weekprice)

    fig = Figure(figsize=(6,5))#increase to make plot bigger
    fig.patch.set_facecolor('black')
    a = fig.add_subplot(111)#scale??? bigger the number, the smaller the size
    def weekgraph():
        try:
            canvas.delete('all')
        except:
            pass
        a.plot(week('^IXIC')[0],week('^IXIC')[1],color='#E5CFAD')
        a.plot(week('^DJI')[0],week('^DJI')[1],color='#D392A4')
        a.plot(week('^GSPC')[0],week('^GSPC')[1],color='#98B7C3')
        a.set_facecolor('black')
        a.set_title ("Market", fontsize=14, color = "white")
        a.set_xlabel("Hour", fontsize=14)  
        a.xaxis.label.set_color('white')
        a.tick_params(axis='x', colors='white')
        a.tick_params(axis='y', colors='white')
        canvas = FigureCanvasTkAgg(fig, master=market)
        canvas.get_tk_widget().place(x=100,y=100)
        canvas.draw()

    def yeargraph():
        try:
            canvas.delete('all')
        except:
            pass
        a.plot(year('^IXIC')[0],year('^IXIC')[1],color='#E5CFAD')
        a.plot(year('^DJI')[0],year('^DJI')[1],color='#D392A4')
        a.plot(year('^GSPC')[0],year('^GSPC')[1],color='#98B7C3')
        a.set_facecolor('black')
        a.set_title ("Market", fontsize=14, color = "white")
        a.set_xlabel("5 Days", fontsize=14)  
        a.xaxis.label.set_color('white')
        a.tick_params(axis='x', colors='white')
        a.tick_params(axis='y', colors='white')
        canvas = FigureCanvasTkAgg(fig, master=market)
        canvas.get_tk_widget().place(x=100,y=100)
        canvas.draw()
    def daygraph():
        try:
            canvas.delete('all')
        except:
            pass
        a.plot(day('^IXIC')[0],day('^IXIC')[1],color='#E5CFAD')
        a.plot(day('^DJI')[0],day('^DJI')[1],color='#D392A4')
        a.plot(day('^GSPC')[0],day('^GSPC')[1],color='#98B7C3')
        a.set_facecolor('black')
        a.set_title ("Market", fontsize=14, color = "white")
        a.set_xlabel("5 minutes", fontsize=14)  
        a.xaxis.label.set_color('white')
        a.tick_params(axis='x', colors='white')
        a.tick_params(axis='y', colors='white')
        canvas = FigureCanvasTkAgg(fig, master=market)
        canvas.get_tk_widget().place(x=100,y=100)
        canvas.draw()

    Button(market, text='Past Day',fg='black', bg='grey', relief=FLAT, command=lambda:daygraph()).place(x=750,y=150)
    Button(market, text='Past 5 Days',fg='black', bg='grey', relief=FLAT, command=lambda:weekgraph()).place(x=810,y=150)
    Button(market, text='Past Year',fg='black', bg='grey', relief=FLAT, command=lambda:yeargraph()).place(x=885,y=150)  
    

    legend1 = tkinter.Text(market, height=1, width=7, bg = '#E5CFAD', fg = 'black', relief=FLAT)
    legend1.configure(font=("Calibri", 15, ""))
    legend1.insert(tkinter.END, "NASDAQ")
    legend1.place(x=750,y=300)
    legend1.config(state=DISABLED)

    legend2 = tkinter.Text(market, height=1, width=9, bg = '#D392A4', fg = 'black', relief=FLAT)
    legend2.configure(font=("Calibri", 15, ""))
    legend2.insert(tkinter.END, "Dow Jones")
    legend2.place(x=750,y=330)
    legend2.config(state=DISABLED)

    legend3 = tkinter.Text(market, height=1, width=8, bg = '#98B7C3', fg = 'black', relief=FLAT)
    legend3.configure(font=("Calibri", 15, ""))
    legend3.insert(tkinter.END, "S & P 500")
    legend3.place(x=750,y=360)
    legend3.config(state=DISABLED)


def updatePortfolio():
    global equity
    currentPrice =0
    for key in prices:
        prices[key]=get_live_price(key)
        currentPrice+=float(prices[key])*float(shares[key])
    if currentPrice!=equity:
        equity = currentPrice

def raise_portfolio():
    global wlist
    wlist = list(OrderedDict.fromkeys(wlist))
    global visible
    visible = 'portfolio'
    print('now on PORTFOLIO')
    portfolio.tkraise()
    equity_txt = tkinter.Text(portfolio, bg = 'black', fg = 'grey', relief=FLAT)
    equity_txt.configure(font=("Calibri", 30, ""))
    equity_txt.insert(tkinter.END, "Your Equity:\n$")
    equity_txt.insert(tkinter.END, equity)
    equity_txt.tag_add("start", "2.0", "3.0")#select tag indexes (lines 2-3)
    equity_txt.tag_config("start", background="black", foreground="white",font=("Calibri", 40, "bold"))
    equity_txt.place(x=100,y=100)
    equity_txt.config(state=DISABLED)
    your_stocks = tkinter.Text(portfolio, height=1, bg = 'black', fg = 'white', relief=FLAT)
    your_stocks.configure(font=("Calibri", 35, ""))
    your_stocks.insert(tkinter.END, "Your Stocks:")
    your_stocks.place(x=100,y=230)
    your_stocks.config(state=DISABLED)
        
    frame_canvas = Frame(portfolio)# Create a frame for the canvas with non-zero row&column weights
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
    pbuttons = [[Button() for j in range(columns)] for i in range(rows)]#creating the empty slots
    for i in range(0, rows):
        for j in range(0, columns):
            
            try:
                ticker = yf.Ticker(plist[index])
                #name, ticker
                #share price x amount of shares
                #profit amount profit %
                #filling the slots in
                pbuttons[i][j].config(text=(plist[index]+"\n$"+
                                    str(round(get_live_price(plist[index]),2)) +'\n' +
                                    str(round(get_live_price(plist[index]) - int(ticker.history(period='1d')['Open']),2)) +
                                    ' (' +str(round(get_live_price(plist[index])/int(ticker.history(period='1d')['Open']),2))+
                                    '%)' + "\n" + names[plist[index]]))
                index+=1
            except:
                #once the index is invalid/plist is out of items, break loop because all slots are filled
                break
    frame_buttons.update_idletasks()# Update buttons frames idle tasks to let tkinter calculate buttons sizes
    first5columns_width = sum([pbuttons[0][j].winfo_width() for j in range(0, columns)])# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
    first5rows_height = sum([pbuttons[i][0].winfo_height() for i in range(0, rows)])
    frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                        height=first5rows_height)
    canvas.config(scrollregion=canvas.bbox("all"))# Set the canvas scrolling region
    frame_canvas.place(x=100,y=300)#plot
    updatepStocks()
raise_portfolio()
raise_watchlist()
raise_home()
def write():
    #Writes data into data.txt 
    print('saving data.....')
    prev_bal = int(datafile[5])
    bal = cur_bal_txt1.cget('text')[1:]
    f = open(os.path.dirname(os.path.abspath(__file__)) + "\data.txt", 'r+')#Fi     nding file apth
    f.truncate(0)#Deletes content
    f.write(str(wlist).replace(' ','')+'\n')
    f.write(str(plist).replace(' ','')+'\n')
    invested_before = {}
    for index in wlist:
        invested_before[index] = float(get_live_price(index)) * float(shares[index])
    f.write(str(invested_before).replace(' ','')+'\n')
    f.write(str(shares).replace(' ','')+'\n')
    f.write(str(cur_bal_txt1.cget('text'))[1:]+'\n')
    f.write(str(prev_bal))
    f.close()
    root.after(10000, write)
    
write()
#Launch Porgram
root.mainloop()
