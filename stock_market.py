import requests
import dateutil.parser
from datetime import timedelta

class Stocks:
    def __init__(self):
        self.url = 'http://finance.yahoo.com/webservice/v1/symbols/{}/quote'
        self.headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MotoG3 Build/MPI24.107-55) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36', 'accept':'application/json', 'Content-type':'application/json'}
        self.payload = {'format': 'json', 'view': 'detail'}

# Get a string with a stock information ticker
# symbols is a dictionary where the key is the stock symbol and the value is the display name 

    def getStockInfo(self, symbols):
        try:
           self.symbollist = ",".join(symbols.keys()) 
           self.response = requests.get(self.url.format(self.symbollist), headers=self.headers, params=self.payload)
           self.quotelist = self.response.json()['list']['resources']       
           self.textback = ''
           for aquote in self.quotelist:
              #if dateutil.parser.parse(aquote['resource']['fields']['utctime']).timedelta(
              self.textback = self.textback + symbols[aquote['resource']['fields']['symbol']] + ' ' + "{0:+.02f}".format(float(aquote['resource']['fields']['chg_percent'])) + '%    '
           return self.textback 
        except:
           return 'Unavailable'
