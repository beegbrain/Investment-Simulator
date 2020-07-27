import json

#save data
userDataToSave = {'stocks':["AAPL", "TSLA"], 'watchlist':["TSLA", "AMZN"], 'money':1000000}

with open('InvestmentSimUserData.json', 'w') as file:
    json.dump(userDataToSave, file)
    file.close()
   
#load data
file = open('InvestmentSimUserData.json')
userData = json.load(file)
file.close()

print(userData)

    

