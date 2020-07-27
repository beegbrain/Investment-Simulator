import json
import pathlib

filePath = pathlib.Path().absolute()

class UserData:
    def __init__(self, stocks, watchlist, money):
        self.stocks = stocks
        self.watchlist = watchlist
        self.money = money
        
userData = UserData([],[],0)

#save data
userDataToSave = {'stocks':["AAPL", "TSLA"], 'watchlist':["TSLA", "AMZN"], 'money':1000000}

with open(r"{}InvestmentSimUserData.json".format(filePath), 'w') as file:
    json.dump(userDataToSave, file)
    file.close()
   
#load data
with open(r"{}InvestmentSimUserData.json".format(filePath), 'r') as file:
    loadedData = json.load(file)
    file.close()
    
    #parse data
    userData.stocks = loadedData['stocks']
    userData.watchlist = loadedData['watchlist']
    userData.money = loadedData['money']

    print(userData.stocks)

    

