
# Alfred657 #

A small digtal voice assistent suitable to run on a Raspberry Pi.

## Setup ##

### You need espeek ###

> sudo apt install espeak

### Flask ###

> sudo apt install python3-flask

### Pip ###

> sudo apt install python3-pip

### Python [MediaWiki](https://pymediawiki.readthedocs.io/en/latest/index.html) ###

> sudo pip3 install pymediawiki

### wordlist

> apt-cache search wordlist

> sudo apt install wbritish

> sudo apt install wswedish

> sudo select-default-wordlist

### run ###

``` Python
python3 -c 'import os; print(os.urandom(16))'
```

> and set the output as app.secret_key

### and then run ###

> python3 clue.py &

----

## RaspberryPi ##

### [To set it to start on boot up](http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/scripts "Setup") ###

>sudo chmod 755 startup_script
>
>sudo nano /etc/rc.local

at the end of the file but before "exit 0" add

>/home/pi/projects/Alfred657/startup_script

## Audio problems on Raspberry Pi ##

### Volume settings ###

> amixer scontrols
>
> amixer sget 'PCM'
>
> amixer sset 'PCM' 50%

### [Audio Output](https://www.raspberrypi.org/documentation/configuration/audio-config.md "Audio Output") ###

> amixer cset numid=3 2

 Here the output is being set to 2, which is HDMI.

 Setting the output to 1 switches to analogue (headphone jack).

 The default setting is 0 which is automatic.

----

### Startup with browser ###

> sudo nano ~/.config/lxsession/LXDE-pi/autostart

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

* exception handling and logging.

* /speak/ responses
