import spidev
import sys
import time

from vfd import VFD
from stock_market import Stocks
from weather import Weather
from datetime import datetime
from datetime import timedelta

displaySize = 16
darkTimeSeconds = 60 * 15 
vfd = VFD(0,0)
stepDelay = 0.20
tickerEndPause = 4 
tickerRounds = 3

# Stocks config
stockM = Stocks()
stock_symbols = {'^GSPC':'S&P 500','^DJI':'Dow 30','^IXIC':'Nasdaq','^RUT':'Rusell 2000','NKE':'Nike, Inc.'}
lastStockDay = 5 # firday=5

# Weather config
weatherI = Weather()
location='Beaverton, OR'

try:
   while True:
      
      # calculate the next execution time
      endTime = datetime.now() + timedelta(0,darkTimeSeconds)
      
      # check latest stock info, if it is a weekday 
      if datetime.now().weekday() < lastStockDay:
         ticker = stockM.getStockInfo(stock_symbols)
      
      # check latest weather info
      weatherTicker = weatherI.getWeatherInfo(location)
      
      for j in range (0, tickerRounds):

         # Update current time
         vfd.setPosition(0,0)
         vfd.writeStr(datetime.strftime(datetime.now(), '%b/%d  %I:%M %p')) 

         if datetime.now().weekday() < lastStockDay:
       
            if len(ticker) <= displaySize :
               vfd.setPosition(0,1)
               vfd.writeStr(ticker)
               time.sleep(tickerEndPause)

            else:
               for n in range (0, len('   ' + ticker)-displaySize):
                  vfd.setPosition(0,1)
                  vfd.writeStr(('   '+ticker)[n:n+displaySize])
                  time.sleep(stepDelay)
               time.sleep(tickerEndPause)

         if len(weatherTicker) <= displaySize :
            vfd.setPosition(0,1)
            vfd.writeStr(weatherTicker.center(displaySize))
            time.sleep(tickerEndPause)

         else:
            for n in range (0, len('   '+weatherTicker)-displaySize):
               vfd.setPosition(0,1)
               vfd.writeStr(('   '+weatherTicker)[n:n+displaySize])
               time.sleep(stepDelay)
         
         time.sleep(tickerEndPause)
      
      vfd.cls()

      while datetime.now() < endTime:
         time.sleep(1)

finally:
   vfd.cls()
