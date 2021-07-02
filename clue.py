# -*- coding: utf-8 -*-
import os
from datetime import datetime
import random

from icalendar import Calendar
from datetime import datetime
from pytz import UTC # timezone
import requests
try:
    from mediawiki import MediaWiki
    from mediawiki.exceptions import DisambiguationError
    wp_imported = True
except ModuleNotFoundError:
    wp_imported = False

from flask import (
    Flask,
    request, abort,
    render_template,
    session
    )

app = Flask(__name__)

app.secret_key = b'dumboPassword'

wikiurl = 'https://en.wikipedia.org/w/api.php'

cal_url = u'https://calendar.google.com/calendar/ical/sv.swedish%23holiday%40group.v.calendar.google.com/public/basic.ics'


def get_random_word():
    word_file = '/usr/share/dict/words'
    WORDS = open(word_file).read().splitlines()
    r_word = random.choice(WORDS)
    return r_word


def get_wikipedia_article(s_word):
    try:
        wikipedia = MediaWiki(url=wikiurl)
        wp_words = wikipedia.search(s_word, results=1)
        wp_article = wikipedia.page(wp_words[0])
        return wp_article
    except DisambiguationError as e:
        wp_article = wikipedia.page(random.choice(e.options))
        return wp_article
    except Exception as e:
        print(e)
        return False


@app.route('/', methods=['GET'])
def index():
    try:
        if cal_url:
            now = datetime.now()
            r = requests.get(cal_url)
            cal_events = []
            gcal = Calendar.from_ical(r.content)
            for component in gcal.walk():
                if component.name == "VEVENT":
                    if component.get('dtstart').dt >= now.date() and component.get('dtstart').dt.year <= now.year :
                        cal_events.append([component.get('dtstart').dt, component.get('summary')])
            cal_events.sort(key=lambda e:e[0])
    except Exception as e:
        print(e)
    return render_template('index.html', cal_events=cal_events)


@app.route('/wiki/', methods=['GET'])
def wiki():
    wp_article = False
    r_word = False
    for x in range(5):
        try:
            r_word = get_random_word()
            if wp_imported:
                wp_article = get_wikipedia_article(r_word)
                break
            else:
                break
        except Exception as e:
            print(e)
    return render_template('wiki.html',
        r_word=r_word,
        wp_article=wp_article)


@app.route('/talk/', methods=['GET', 'POST'])
def talk():
    if request.method == 'POST':
        string = request.form['string']
        session['string'] = string
        try:
            os.system('espeak -ven+m6 -s125 "{0}" '.format(string))
            return render_template('talk.html')
        except Exception:
            # logging ?
            return abort(400)
    return render_template('talk.html')


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


@app.route('/time/', methods=['GET'])
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
