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
#Misc libraries
from collections import Counter 

root = tkinter.Tk()
root.title("Investment Simulator")
root.geometry('1280x700')
root.configure(bg='black')
home = Frame(root,width=1280, height=700)
watchlist = Frame(root,width=1280, height=700)
market = Frame(root,width=1280, height=700)
portfolio = Frame(root,width=1280, height=700)
graphing = Frame(root,width=1280, height=700)
global wlist_index
wlist_index = 0
def raise_frame(frame):
    frame.tkraise() #Brings desired frame to the top
    
for frame in (home, watchlist, market, portfolio, graphing):
    #Set frame to fill page
    frame.configure(bg="black") #Background Color
    frame.grid(sticky='nswe')
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=0,column=1)

    #Page Buttons
    Button(frame, text='Home',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(home)).place(x=50,y=50)
    Button(frame, text='Watchlist',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(watchlist)).place(x=104,y=50)    
    Button(frame, text='Market',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(market)).place(x=170,y=50)
    Button(frame, text='Portfolio',fg='black', bg='grey', relief=FLAT, command=lambda:raise_frame(portfolio)).place(x=225,y=50)    
    
def watchlist_page(name):   #EDIT GRAPH HERE 
    raise_frame(graphing)#Keep this here
    #Edit everything after this line  (make sure the frame name is graphing, not root/master/self/frame .....)
    x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
    p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
        19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

    fig = Figure(figsize=(3,3))#increase to make plot bigger
    a = fig.add_subplot(111)#scale??? bigger the number, the smaller the size
    a.scatter(v,x,color='red')
    a.plot(p, range(2 +max(x)),color='blue')
    
    a.set_title ("Estimation Grid", fontsize=16)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)

    #Watchlist(Home)
watchlist_txt = tkinter.Text(home, height = 1, width = len("Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
watchlist_txt.configure(font=("Calibri", 30, ""))
watchlist_txt.insert(tkinter.END, "Watchlist:")
watchlist_txt.place(relx=0.5, y=250, anchor=CENTER)
watchlist_txt.config(state=DISABLED)
invested_before = {"AAPL":384.77,"TSLA":1627.63,"NFLX":410.34,"INTL":398.93,"GOOGL":1453}  #The day before? depends... you choose what data to put
invested_curr = {"AAPL":390,"TSLA":1617,"NFLX":400,"INTL":405,"GOOGL":1343}   #Current invested profit
names = {"AAPL":"Apple Inc.","TSLA":"Tesla Inc.","NFLX":"Netflix Inc.","INTL":"Intel Inc.","GOOGL":"Google"}   #Put the names you want to show here
wlist = ["AAPL","TSLA","NFLX","INTL","GOOGL"]#current watchlist
k = Counter(invested_curr) 
highest = k.most_common(3) # Finding 3 highest values 
x_coor=0
scroll_y = tkinter.Scrollbar(home, orient="vertical")
scroll_y.configure(bg='black')
for set in highest:
    button = Button(scroll_y, bg="white", relief=FLAT, text = (set[0]+"\n$"+str(set[1]) +"   "  + str(round(set[1] - invested_before[set[0]],2)) + "\n" + names[set[0]]))
    button.place(x=x_coor)
    x_coor += len(set[0]+"\n$"+str(set[1]) +"   "  + str(round(set[1] - invested_before[set[0]],2)) + "\n" + names[set[0]])*2.7
scroll_y.configure(width=x_coor-9)
scroll_y.place(relx=0.485, y=330, anchor=CENTER)

    #Edit
edit = tkinter.Button(home, text="edit",relief=FLAT, width = 5, command = "send to watchlist edit")
edit.place(relx=0.485, y=285, anchor = CENTER)


#Market

#Watchlist
wlist_txt = tkinter.Text(watchlist, height = 1, width = len("Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
wlist_txt.configure(font=("Calibri", 30, ""))
wlist_txt.insert(tkinter.END, "Watchlist:")
wlist_txt.place(x=100,y=100)
wlist_txt.config(state=DISABLED)

    canvas = FigureCanvasTkAgg(fig, master=graphing)
    canvas.get_tk_widget().place(x=100,y=100)
    canvas.draw()
    
if True:#Home Page
        #Balance
    balance = 100000000
    cur_bal_txt = tkinter.Text(home, height = 3, bg = 'black', fg = 'grey', relief=FLAT)
    cur_bal_txt.configure(font=("Calibri", 30, ""))
    cur_bal_txt.insert(tkinter.END, "Your Balance:\n")
    cur_bal_txt.insert(tkinter.END, '$' + str(balance))
    cur_bal_txt.tag_add("start", "2.0", "3.0")#select tag indexes (lines 2-3)
    cur_bal_txt.tag_config("start", background="black", foreground="white",font=("Calibri", 40, "bold"))#change tag to white
    cur_bal_txt.place(x=100,y=100)
    cur_bal_txt.config(state=DISABLED)#No Editing text box
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

        #Watchlist(Home)
    watchlist_txt = tkinter.Text(home, height = 1, width = len("Priority Watchlist:"), bg = 'black', fg = 'white', relief=FLAT)
    watchlist_txt.configure(font=("Calibri", 30, ""))
    watchlist_txt.insert(tkinter.END, "Priority Watchlist:")
    watchlist_txt.place(relx=0.5, y=250, anchor=CENTER)
    watchlist_txt.config(state=DISABLED)
    invested_before = {"AAPL":384.77,"TSLA":1627.63,"NFLX":410.34,"INTL":398.93,"GOOGL":1453}  #The day before? depends... you choose what data to put
    invested_curr = {"AAPL":390,"TSLA":1617,"NFLX":400,"INTL":405,"GOOGL":1343}   #Current invested profit
    names = {"AAPL":"Apple Inc.","TSLA":"Tesla Inc.","NFLX":"Netflix Inc.","INTL":"Intel Inc.","GOOGL":"Google"}   #Put the names you want to show here
    wlist = ["AAPL","TSLA","NFLX","INTL","GOOGL"]#current watchlist
    k = Counter(invested_curr) 
    highest = k.most_common(3) # Finding 3 highest values 
    x_coor=0
    scroll_y = tkinter.Scrollbar(home, orient="vertical")
    scroll_y.configure(bg='black')
    index = 0
    for set in highest:
        Button(scroll_y, bg="white", relief=FLAT, command=lambda set=set:watchlist_page(set[0]),text = (set[0]+"\n$"+str(set[1]) +"   "  + str(round(set[1] - invested_before[set[0]],2)) + "\n" + names[set[0]])).place(x=x_coor)
        x_coor += len(set[0]+"\n$"+str(set[1]) +"   "  + str(round(set[1] - invested_before[set[0]],2)) + "\n" + names[set[0]])*2.7
    scroll_y.configure(width=x_coor-9)
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
                #filling the slots in
                buttons[i][j] = Button(frame_buttons, bg='white',relief=FLAT,command=lambda index=index:watchlist_page(wlist[index]), text=(wlist[index]+"\n$"+str(invested_curr[wlist[index]]) +"   "  + str(round(invested_curr[wlist[index]] - invested_before[wlist[index]],2)) + "\n" + names[wlist[index]]))
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

#Launch Porgram
home.tkraise()
root.mainloop()
