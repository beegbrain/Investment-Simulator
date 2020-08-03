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
    elif float(numField.get())<=0:
        mb.showerror("Error", "You cannot purchase a nonpositive amount of stocks")
        return()
    elif int(numField.get()) != float(numField.get()):
        mb.showerror("Error", "You cannot buy a noninteger amount of stocks")
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
