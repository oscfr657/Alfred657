import os
from datetime import datetime

from flask import (
    Flask,
    request, jsonify, abort,
    render_template,
    session, redirect, url_for, escape
    )

app = Flask(__name__)


app.secret_key = b'dumboPassword'


@app.route('/', methods=['GET'])
def index():
    name = session.get('username', False)
    return render_template('index.html', name=name)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    name = session.get('username', False)
    if name:
        os.system('espeak -ven+m6 -s125 "Hello {0}" '.format(name))
    if request.method == 'POST':
        username = request.form['username']
        os.system('espeak -ven+m6 -s125 "Hello {0}" '.format(username))
        name = username
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('login.html', name=name)


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/talk/', methods=['GET', 'POST'])
def talk():
    name = session.get('username', False)
    if request.method == 'POST':
        string = request.form['string']
        session['string'] = string
        try:
            os.system('espeak -ven+m6 -s125 "{0}" '.format(string))
            return render_template('talk.html', name=name)
        except Exception:
            # logging ?
            return abort(400)
    return render_template('talk.html', name=name)


@app.route('/speak/', methods=['GET', 'POST'])
def speak():
    if request.method == 'POST':
        try:
            jsonfile = request.get_json()
            string = jsonfile['string']
            os.system('espeak -ven+m6 -s125 "{0}"'.format(string))
        except Exception:
            # logging ?
            return abort(400)
        return 'Success'
    else:
        return 'Fail'


@app.route('/time', methods=['GET'])
def time():
    now = datetime.now()
    minute = now.minute
    if minute < 10:
        minute = 'O ' + str(minute)
    time_string = '{0} {1}'.format(now.hour, minute)
    try:
        os.system('espeak -ven+m6 -s125 "The time is {0}"'.format(time_string))
    except Exception:
        return 'Fail'
    return 'Success'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
