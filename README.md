
# Alfred657 #

A small digtal voice assistent suitable to run on a Raspberry Pi.

## Requirements

    Python >= 3.9.0

## Setup ##

### You need espeek ###

> sudo apt install espeak

### Flask ###

> sudo apt install python3-flask

### Pip ###

> sudo apt install python3-pip

### icalendar ###

> sudo apt install python3-icalendar

### Python [MediaWiki](https://pymediawiki.readthedocs.io/en/latest/index.html) ###

> sudo pip3 install pymediawiki

### wordlist ###

> apt-cache search wordlist
>
> sudo apt install wbritish
>
> sudo apt install wswedish
>
> sudo select-default-wordlist

### Flask app secret key ###

``` Python
python3 -c 'import os; print(os.urandom(16))'
```

> and set the output as app.secret_key

### Run ###

> python3 clue.py &

----

## RaspberryPi ##

### Copy from your local mashine to the Raspberry Pi ###

    Yuu can use scp:
    scp -r static/ pi@10.0.0.2:/home/pi/projects/Alfred657/
    scp -r templates/ pi@10.0.0.2:/home/pi/projects/Alfred657/
    scp clue.py  pi@10.0.0.2:/home/pi/projects/Alfred657/

### [To set it to start on boot up](http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/scripts "Setup") ###

>sudo chmod 755 startup_script
>
>sudo nano /etc/rc.local

at the end of the file but before "exit 0" add

>/home/pi/projects/Alfred657/startup_script

### Startup with browser ###

    sudo mkdir ~/.config/lxsession/LXDE-pi
    sudo nano ~/.config/lxsession/LXDE-pi/autostart

add

``` bash
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@point-rpi
@xset s off
@xset -dpms
@xset s noblank
@chromium-browser --kiosk --incognito http://localhost:5000
```

### [Audio Output](https://www.raspberrypi.org/documentation/configuration/audio-config.md "Audio Output") ###

> amixer cset numid=3 2

 Here the output is being set to 2, which is HDMI.

 Setting the output to 1 switches to analogue (headphone jack).

 The default setting is 0 which is automatic.

### Volume settings ###

> amixer scontrols
>
> amixer sget 'PCM'
>
> amixer sset 'PCM' 50%

### Screen ###

#### Screen brightness ####

> sudo nano /sys/class/backlight/rpi_backlight/brightness
>
> 0 - 255

### [Screen rotation](https://www.raspberrypi.com/documentation/accessories/display.html) ###

#### The Raspberry Pi touchscreen
    
    sudo nano /boot/config.txt
    display_lcd_rotate=2
    lcd_rotate=2

##### [Bug workaround](https://github.com/raspberrypi/linux/issues/4686) ####

    sudo nano /boot/config.txt
    dtparam=i2c_vc_baudrate=5000
    lcd_rotate=2

## Ubuntu 24.04 ##

### alfred.service ###

    sudo cp alfred.service.example alfred.service

    Update the paths in alfred.service

    sudo cp alfred.service /etc/systemd/system/

    sudo systemctl daemon-reload

    sudo systemctl start alfred.service

    sudo systemctl status alfred.service

    sudo systemctl stop alfred.service

    sudo systemctl restart alfred.service

    sudo systemctl enable alfred.service

    sudo systemctl disable alfred.service

----

## For development and testing ##

> pip install requests, json
>
> python3

``` python
import requsts, json
r = requests.post('http://localhost:5000/speak/',
                  json = {'key':'It is time for some testing.'})
```

or test it localy

``` python
import os
os.system('espeak -ven+m6 -s125 "It is time for some testing." ')
```

----

## TODO ##

* setting for voice type and number ?

* /speak/ responses
