import requests

class Stocks:
    def __init__(self):
        self.url = 'http://finance.yahoo.com/webservice/v1/symbols/{}/quote'
        self.headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MotoG3 Build/MPI24.107-55) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36', 'accept':'application/json', 'Content-type':'application/json'}
        self.payload = {'format': 'json', 'view': 'detail'}
    def getStockInfo(self, symbols):
        self.symbollist = ",".join(symbols) 
        self.response = requests.get(self.url.format(self.symbollist), headers=self.headers, params=self.payload)
        self.quotelist = self.response.json()['list']['resources']       
        self.textback = '    '
        for aquote in self.quotelist:
           self.textback = self.textback + aquote['resource']['fields']['name'].replace('&amp;','&') + ' ' + "{0:+.02f}".format(float(aquote['resource']['fields']['chg_percent'])) + '%    '
        return self.textback 
