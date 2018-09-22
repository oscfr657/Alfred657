# You need espeek.
# sudo apt install espeak
# and Flask
# sudo apt install python3-flask
# run
# sudo python3 clue.py

# ---- hmm.. remove ------
# export FLASK_APP=clue.py
# export FLASK_ENV=development
# flask run --host=0.0.0.0:80
# ------------------------


import os

from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route('/speak/', methods=['GET', 'POST'])
def speak():
    if request.method == 'POST':
        try:
            jsonfile = request.get_json()
            key = jsonfile['key']
            os.system('espeak -ven+m6 -s125 "{0}" '.format(key))
        except Exception as e:
            return abort(400)
        return 'Success'
    else:
        return 'Fail'


# for testing
# pip install requests
# r = requests.post('http://192.168.1.5:80/speak/', json = {'key':'It is time for some testing.'})
# or
# import os
# os.system('espeak -ven+m6 -s125 "It is time for dishes." ')


@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
