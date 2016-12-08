# Raspberry PI Nightstand Clock project

The objective of this project is to create a cool nightstand clock 
that can provide me with additional relevant information for my day 
and at the same time be discrete so it does not light up the room
when I am trying to sleep.

# Current state:

I had a Raspberry Pi B+ laying around from a previous project so I dusted it
and flashed a 2 GB Micro SD card with Raspbian Jesse Lite. For the display
I chose a Noritake Vacumm Flourecent Display (VFD) because I like the retro look.
I am also using a USB Wi-fi dongle.
For the case I am using a temporary setup made with Legos. Here is how it looks like right now:

![Imgur](http://i.imgur.com/ZFq8nve.jpg)

Here is what it does right now:

 * Display date and time using a Vacuum Fluorescent Display (VFD) controlled by a Raspberry PI using a SPI interface 
 * Able to charge an iPhone via USB and lightning cable
 * Display latest stock market information

And this is the To-Do list:

 * By default the display is off and it gets activated by a motion sensor on top 
 * Sync time and date with NTP
 * Display stock market information only if it is a traiding day
 * Display local wather info

# Setup Steps:

1. Install fresh Raspbian Jesse lite image, resize partition, set password.
1. Using wired ethernet update installation:
	sudo apt-get update
	sudo apt-get dist-upgrade
1. Configure wi-fi
	https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
1. Using raspi-config enable SPI interface
1. Follow:
	http://www.smbaker.com/interfacing-a-vfd-display-to-the-raspberry-pi
1. Setup script to start on boot:
	Edit `/etc/local.rc` and add at the end `sudo python /home/pi/vfdclock/clock.py`
