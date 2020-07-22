import time
import yfinance as yf

search = True

while search:
    msft = yf.Ticker("TSLA")
    
    # get stock info
    msft.info
    
    # get historical market data
    hist = msft.history(period="day", interval = "1m")
    print(hist)
    time.sleep(5)


