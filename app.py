import os
import json

from flask import Flask, render_template, url_for, request
from socket import gethostname # For checking if it's running on pythonanywhere

from settings import APP_STATIC


app = Flask(__name__)
#TODO
# Currently just checks to see if app is running on pythonanywhere (intended
# quick deploy location) and turns debug on if not true. Later refactor for
# more robust deployment options.
if 'liveconsole' not in gethostname():
    app.config["DEBUG"] = True


#TODO doc this
def readData():
    with open(os.path.join(APP_STATIC, 'data.json')) as f:
        return json.load(f)


@app.route('/')
def index():
    data = readData()
    return render_template('index.html',
                           static_questions=data['static_questions'],
                           custom_questions=data['custom_questions'])

@app.route('/add', methods=['POST'])
def add():
    data = readData()
    data['custom_questions'].append(request.form['q'])

    with open(os.path.join(APP_STATIC, 'data.json'), 'w') as f:
        f.write(json.dumps(data))

    return ('', 204) # Intentional empty response
