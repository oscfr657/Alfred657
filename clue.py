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
            # logging ?
            return abort(400)
        return 'Success'
    else:
        return 'Fail'


@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
