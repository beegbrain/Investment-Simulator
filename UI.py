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

#Grabbing Data
datafile = open("data.txt").read().split()
wlist = eval(datafile[0])#current watchlist
invested_before = eval(datafile[1])  #The day before? depends... you choose what data to put
shares = eval(datafile[2])
prices = dict()
names = dict()
for index in wlist:
    print(index)
    prices[index] = get_live_price(index)
    stock = yf.Ticker(index)
    names[index] = stock.info['shortName']





global wlist_index
wlist_index = 0
def raise_frame(frame):
    frame.tkraise() #Brings desired frame to the top

for frame in (home, watchlist, market, portfolio, graphing, search):
    #Set frame to fill page
    frame.configure(bg="black") #Background Color
    frame.grid(row=0,column=0,sticky="nsew")
    #Page Buttons
    Button(frame, text='Home',font=("Calibri", 25, ""),fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).place(x=50,y=20)
    Button(frame, text='Market',font=("Calibri", 25, ""),fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(watchlist)).place(x=180,y=20)    
    Button(frame, text='Portfolio',font=("Calibri", 25, ""),fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).place(x=330,y=20)
    Button(frame, text='Search',font=("Calibri", 25, ""),fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(search)).place(x=500,y=20)
    
def graph_page(name):   #EDIT GRAPH HERE 
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
    
if True:#Home Page
        #Balance
    prev_bal  = int(datafile[4])
    balance = int(datafile[3])
    cur_bal_txt = tkinter.Text(home, height = 3, bg = 'black', fg = 'grey', relief=FLAT)
    cur_bal_txt.configure(font=("Calibri", 30, ""))
    cur_bal_txt.insert(tkinter.END, "Your Balance:\n")
    cur_bal_txt.insert(tkinter.END, '$' + str(balance))
    cur_bal_txt.tag_add("start", "2.0", "3.0")#select tag indexes (lines 2-3)
    cur_bal_txt.tag_config("start", background="black", foreground="white",font=("Calibri", 40, "bold"))#change tag to white
    cur_bal_txt.place(x=100,y=100)
    cur_bal_txt.config(state=DISABLED)#No Editing text box
        #Balance with stocks
    bal_stocks = int(datafile[5])
    bal_stocks_txt = tkinter.Text(home, height = 3, bg = 'black', fg = 'grey', relief=FLAT)
    bal_stocks_txt.configure(font=("Calibri", 30, ""))
    bal_stocks_txt.insert(tkinter.END, "With Stocks: \n")
    bal_stocks_txt.insert(tkinter.END, '$' + str(bal_stocks))
    bal_stocks_txt.tag_add("start", "2.0", "3.0")
    bal_stocks_txt.tag_config("start", background="black", foreground="white",font=("Calibri", 40, "bold"))
    bal_stocks_txt.place(x=500,y=100)
    bal_stocks_txt.config(state=DISABLED)
            #Bal Increase Today
    inc_num = balance - prev_bal
    today = tkinter.Text(home, height = 3, width = len(str(inc_num)), bg = 'black', fg = 'grey', relief=FLAT)
    today.configure(font=("Calibri", 30, ""))
    today.insert(tkinter.END, "Today:\n")
    today.insert(tkinter.END, ' +' + str(inc_num))
    today.tag_add("start", "2.0", "3.0")
    today.tag_config("start", background="#32CD32", foreground="white",font=("Calibri", 20, "bold"))
    today.place(x=900,y=100)
    today.config(state=DISABLED)

        #Watchlist(Home)
    watchlist_txt = tkinter.Text(home, height = 1, width = len("Priority Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
    watchlist_txt.configure(font=("Calibri", 30, ""))
    watchlist_txt.insert(tkinter.END, "Priority Watchlist:")
    watchlist_txt.place(relx=0.5, y=250, anchor=CENTER)
    watchlist_txt.config(state=DISABLED)
    k = Counter(invested_before) 
    highest = k.most_common(3) # Finding 3 highest values 
    x_coor=0
    scroll_y = tkinter.Scrollbar(home, orient="vertical")
    scroll_y.configure(bg='black')
    index = 0
    # Show price of stock, profit in %, how many shares
    for set in highest:
        Button(scroll_y, bg="white", relief=FLAT, command=lambda set=set:graph_page(set[0]),text = (set[0]+"\n$"+str(round(prices[set[0]],2)) +"   "  + str(round(shares[set[0]]*prices[set[0]] - invested_before[set[0]],2)) + "\n" + names[set[0]])).pack(side='right',expand=True)
        x_coor += len(set[0]+"\n$"+str(set[1]) +"   "  + str(round(set[1] - invested_before[set[0]],2)) + "\n" + names[set[0]]) * 4
    scroll_y.configure()
    scroll_y.place(relx=0.485, y=330, anchor=CENTER)
    
        #Edit
    more = tkinter.Button(home, text="View All",relief=FLAT, width = 6, command = lambda:raise_frame(watchlist))
    more.place(relx=0.485, y=285, anchor = CENTER)

if True:#Watchlist
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
    buttons = [[Button() for j in range(columns)] for i in range(rows)]#creating the empty slots
    for i in range(0, rows):
        for j in range(0, columns):
            try:
                    #name, ticker
                    #share price x amount of shares
                    #profit amount profit %
                #filling the slots in
                buttons[i][j] = Button(frame_buttons, bg='white',relief=FLAT,command=lambda index=index:graph_page(wlist[index]), text=(wlist[index]+"\n$"+str(round(prices[wlist[index]],2)) +" x "  +str(shares[wlist[index]])+ '\n' + str(round(shares[wlist[index]] * prices[wlist[index]] - invested_before[wlist[index]],2)) + ' (' +str(round(shares[wlist[index]] * prices[wlist[index]]/invested_before[wlist[index]],2))+ '%)' + "\n" + names[wlist[index]]))
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
   
#Market Page
graph = tkinter.Text(market, bg = 'black', fg = 'grey', relief=FLAT,height=1)
graph.configure(font=("Calibri", 30, ""))
graph.insert(tkinter.END, "How do i graph")
graph.place(x=100,y=400)
graph.config(state=DISABLED)

#Portfolio Page
equity = "100,000,000"
equity_txt = tkinter.Text(portfolio, height=2, bg = 'black', fg = 'grey', relief=FLAT)
equity_txt.configure(font=("Calibri", 30, ""))
equity_txt.insert(tkinter.END, "Your Equity:\n")
equity_txt.insert(tkinter.END, "100,000,000")
equity_txt.place(x=100,y=100)
equity_txt.config(state=DISABLED)

#Search Page
edit = Entry(search)
edit.place(relx=0.5,y=50)
edit.focus_set()
butt = Button(search, text='Find')
butt.place(relx=0.4,y=50)
name = list()
def find():
    global name
    name = list()
    query = edit.get()
    response = requests.get("https://ticker-2e1ica8b9.now.sh/keyword/"+query)
    data = response.text.split(',')
    for index in range(0, len(data), 2):
        data[index] = data[index].split(':')
        name.append(data[index][1].replace('"',''))
    return(names) 
butt.config(command=find)
#Launch Porgram
home.tkraise()
root.mainloop()
