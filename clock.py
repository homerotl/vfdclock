import spidev
import sys
import time

from vfd import VFD
from datetime import datetime
from datetime import timedelta

displaySize = 16
darkTimeSeconds = 60 * 5
vfd = VFD(0,0)
stepDelay = 0.25
tickerEndPause = 4 
tickerRounds = 3

ticker = 'Dow +0.01 %    S&P 500 -0.27 %    Nasdaq -1.05 %'

# url = 'http://finance.yahoo.com/webservice/v1/symbols/^GSPC,^RUT/quote'
# headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MotoG3 Build/MPI24.107-55) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36', 'accept':'application/json', 'Content-type':'application/json'}
# payload = {'format': 'json', 'view': 'detail'}
# response = requests.get(url, headers=headers, params=payload)

# print(response.json())

tickerStep = 0

try:
   while True:

      endTime = datetime.now() + timedelta(0,darkTimeSeconds)

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
