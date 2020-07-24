import time
import yfinance as yf
import asyncio

global userStocks
userStocks = ["AAPL", "TSLA", "NFLX", "AMZN"]

async def looper():
    while True:
        global userStocks

        print(userStocks)
        for item in userStocks:
            ticker = yf.Ticker(item)
            print(ticker.history(period="day"))
            
            await asyncio.sleep(0.5)

async def main():
    future = asyncio.ensure_future(looper())
    await asyncio.sleep(5)
    
    global userStocks
    userStocks = ["AAPL", "TSLA", "AMZN", "BA"]
    await asyncio.sleep(10)

    
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
