import spidev
import sys
import time
import RPi.GPIO as GPIO

from vfd import VFD
from stock_market import Stocks
from weather import Weather
from datetime import datetime
from datetime import timedelta

displaySize = 16
vfd = VFD(0,0)
stepDelay = 0.15
tickerEndPause = 3 

# Configure PIR motion detector
PIRport = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIRport, GPIO.IN)

# Stocks config
stockM = Stocks()
stock_symbols = {'^GSPC':'S&P 500','^DJI':'Dow 30','^IXIC':'Nasdaq','^RUT':'Rusell 2000','NKE':'Nike, Inc.'}
lastStockDay = 5 # firday=5

# Weather config
weatherI = Weather()
location='Beaverton, OR'
weatherLatencyMinutes = 10
nextWeatherCheckTime = datetime.now() - timedelta(seconds=1)  

try:

   while True:
      
      inputState = GPIO.input(PIRport)
      
      if inputState == True:

         print('Motion detected')

         # check latest stock info, if it is a weekday 
         if datetime.now().weekday() < lastStockDay:
            ticker = stockM.getStockInfo(stock_symbols)
      
         # check latest weather info
         if datetime.now() > nextWeatherCheckTime : 
            weatherTicker = weatherI.getWeatherInfo(location)
            nextWeatherCheckTime = datetime.now() + timedelta(minutes=weatherLatencyMinutes)
 
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

      else:
         if datetime.now() > nextWeatherCheckTime :
            weatherTicker = weatherI.getWeatherInfo(location)
            nextWeatherCheckTime = datetime.now() + timedelta(minutes=weatherLatencyMinutes) 
         time.sleep(1)
finally:
   vfd.cls()
