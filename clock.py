#
# Raspberry nightstand clock project
#
# * Can charge an iPhone
# * Triggered on button or IR movement sensor:
#
# 	Display time and date
# 	Sync time and date with NTP
# 	Display latest stock market information if it is a traiding day
#	Display local wather info
# 
# Display:
# dd/MM HH/MM
#	
# Steps:
# 1. Install fresh Raspbian Jesse lite image
# 2. Resize part, change password
# 3. Update latest libraries
#	sudo apt-get update
#	sudo apt-get dist-upgrade
# 4. Configure wi-fi
#	https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
# 5. Using raspi-config enable SPI interface
# 6. Follow:
# http://www.smbaker.com/interfacing-a-vfd-display-to-the-raspberry-pi

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
