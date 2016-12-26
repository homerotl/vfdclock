import requests

class Weather:
    def __init__(self):
        self.url = 'https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&u=c'

# Get weather information from Yahoo 
# city is aa string with the city name and state, like 'Austin, TX' 

    def getWeatherInfo(self, city):
        try:
           self.response = requests.get(self.url.format(city))
           self.condition = self.response.json()['query']['results']['channel']['item']['condition']       
           self.textback = self.condition['text'] + ' ' + self.condition['temp'] + ' F'
           return self.textback 
        except:
           return 'Unavailable'
