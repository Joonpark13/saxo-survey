import os
import json

from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from settings import APP_STATIC #TODO Won't need this after implementing db


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # warned by db
db = SQLAlchemy(app)


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


if __name__ == '__main__':
    app.run()