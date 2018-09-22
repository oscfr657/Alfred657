# You need espeek.
# sudo apt install espeak
# and Flask
# sudo apt install python3-flask
# run
# export FLASK_APP=clue.py
# export FLASK_ENV=development
# flask run --host=0.0.0.0:80

import os

from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route('/speak/', methods=['GET', 'POST'])
def speak():
    if request.method == 'POST':
        try:
            jsonfile = request.get_json()
            key = jsonfile['key']
            os.system('espeak -ven+f5 -s110 "{0}" '.format(key))
        except Exception as e:
            return abort(400)
        return 'Success'
    else:
        return 'Fail'


# for testing
# pip install requests
# r = requests.post('http://127.0.0.1:5000/speak/', json = {'key':'It is time for some testing.'})


@app.route('/')
def index():
    return 'Hello world'
