import os
import json

from flask import Flask, render_template, url_for
from socket import gethostname # For checking if it's running on pythonanywhere

from settings import APP_STATIC


app = Flask(__name__)
#TODO
# Currently just checks to see if app is running on pythonanywhere (intended
# quick deploy location) and turns debug on if not true. Later refactor for
# more robust deployment options.
if 'liveconsole' not in gethostname():
    app.config["DEBUG"] = True

@app.route('/')
def index():
    with open(os.path.join(APP_STATIC, 'data.json')) as f:
        data = json.load(f)

    return render_template('index.html', static_questions=data['static_questions'])