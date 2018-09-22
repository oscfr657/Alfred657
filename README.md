
# Alfred657 #

A small digtal voice assistent suitable to run on a Raspberry Pi.

## Setup ##

### You need espeek ###

> sudo apt install espeak

### and Flask ###

> sudo apt install python3-flask

### run ###

> sudo python3 clue.py &

[//]: # (
export FLASK_APP=clue.py
export FLASK_ENV=development
flask run --host=0.0.0.0:80
)

## For development and testing ##

> pip install requests

``` python
r = requests.post('http://192.168.1.5/speak/', json = {'key':'It is time for some testing.'})
```

or test it localy

``` python
import os
os.system('espeak -ven+m6 -s125 "It is time for some testing." ')
```

## Audio problems on Raspberry Pi ##

### Volume settings ###

> amixer scontrols
>
> amixer sget 'PCM'
>
> amixer sset 'PCM' 50%

### [Output](https://www.raspberrypi.org/documentation/configuration/audio-config.md "Output") ###

> amixer cset numid=3 2

 Here the output is being set to 2, which is HDMI.

 Setting the output to 1 switches to analogue (headphone jack).

 The default setting is 0 which is automatic.
