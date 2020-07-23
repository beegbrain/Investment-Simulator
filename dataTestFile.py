import time
import yfinance as yf

import asyncio

search = True

async def looper():
    for i in range(1_000_000_000):
        msft = yf.Ticker("AAPL")
        
        print(msft.history(period="day"))
        
        await asyncio.sleep(0.5)

async def main():
    print('Starting')
    future = asyncio.ensure_future(looper())
    print('Waiting for a few seconds')
    await asyncio.sleep(4)
    print('Cancelling')
    future.cancel()
    print('Waiting again for a few seconds')
    await asyncio.sleep(2)
    print('Done')
    
    
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


print("here")
