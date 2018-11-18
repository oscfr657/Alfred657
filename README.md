
# Alfred657 #

A small digtal voice assistent suitable to run on a Raspberry Pi.

## Setup ##

### You need espeek ###

> sudo apt install espeak

### and Flask ###

> sudo apt install python3-flask

### run ###

> sudo python3 clue.py &

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
## For development and testing ##

> pip install requests, json

``` python
import requsts, json
r = requests.post('http://192.168.1.3/speak/', 
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
