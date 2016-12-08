import spidev
import sys
import time

from vfd import VFD
from stock_market import Stocks
from datetime import datetime
from datetime import timedelta

displaySize = 16
darkTimeSeconds = 60 * 5
vfd = VFD(0,0)
stepDelay = 0.25
tickerEndPause = 4 
tickerRounds = 3
stockM = Stocks()
stock_symbols = ['^GSPC','^DJI','^IXIC','^RUT','NKE']
ticker = stockM.getStockInfo(stock_symbols) 

try:
   while True:

      endTime = datetime.now() + timedelta(0,darkTimeSeconds)
      
      if len(ticker) <= displaySize :
         vfd.setPosition(0,0)
         vfd.writeStr(datetime.strftime(datetime.now(), '%b/%d  %I:%M %p'))
         vfd.setPosition(0,1)
         vfd.writeStr(ticker)

      else:
         for j in range (0, tickerRounds):
            for n in range (0, len(ticker)-displaySize):
               vfd.setPosition(0,0)
               vfd.writeStr(datetime.strftime(datetime.now(), '%b/%d  %I:%M %p'))
               vfd.setPosition(0,1)
               vfd.writeStr(ticker[n:n+displaySize])
               time.sleep(stepDelay)
            time.sleep(tickerEndPause)
         vfd.cls()

      while datetime.now() < endTime:
         time.sleep(1)

finally:
   vfd.cls()
