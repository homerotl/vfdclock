import spidev
import requests
import sys
import time
from vfd import VFD 
from datetime import datetime

vfd = VFD(0,0)
stepDelay = 1 # seconds

# url = 'http://finance.yahoo.com/webservice/v1/symbols/^GSPC,^RUT/quote'
# headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MotoG3 Build/MPI24.107-55) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36', 'accept':'application/json', 'Content-type':'application/json'}
# payload = {'format': 'json', 'view': 'detail'}
# response = requests.get(url, headers=headers, params=payload) 

# print(response.json())

try:
   while True:
      # Start by displaying Hostname
      vfd.setPosition(0,0)
      vfd.writeStr(datetime.strftime(datetime.now(), '%m/%d %I:%M %p'))
      time.sleep(stepDelay)
finally:
   vfd.cls()
