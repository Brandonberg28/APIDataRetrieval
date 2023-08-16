import requests
from bs4 import BeautifulSoup 

#create vars, url and get response 
tickerSymbol = 'COKE' #Roblox!!!
url = 'https://finance.yahoo.com/quote/'+tickerSymbol
response = requests.get(url)

#create soup object to grab data
soup = BeautifulSoup(response.content, 'lxml')

#use Beautiful Soup to display the latest stock price
stockPrice = soup.find('fin-streamer', {'data-field':'regularMarketPrice','data-symbol':tickerSymbol}).text
print(f"{tickerSymbol} Stock price: {stockPrice}")

#Traverse through the HTML tree and display the market cap
marketCap = soup.find('td',{'data-test':'MARKET_CAP-value'}).text
print(f"{tickerSymbol} Market cap: {marketCap}")


