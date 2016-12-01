# Raspberry PI Nightstand Clock project

 * Display date and time using a Vacuum Fluorescent Display (VFD) controlled by a Raspberry PI using a SPI interface 
 * Able to charge an iPhone via USB and lightning cable
 * By default the display is off and it gets activated by a motion sensor on top 
 * Sync time and date with NTP
 * Display latest stock market information if it is a traiding day
 * Display local wather info


# Steps:
1. Install fresh Raspbian Jesse lite image
1. Resize part, change password
1. Update latest libraries
	sudo apt-get update
	sudo apt-get dist-upgrade
1. Configure wi-fi
	https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
1. Using raspi-config enable SPI interface
1. Follow:
	http://www.smbaker.com/interfacing-a-vfd-display-to-the-raspberry-pi
1. Setup script to start on boot:
	Edit `/etc/local.rc` and add at the end `sudo python /home/pi/vfdclock/clock.py`
