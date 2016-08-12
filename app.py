import os

from flask import Flask, render_template, url_for, request
from models import db, Question


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # warned by db
db.init_app(app)


@app.route('/')
def index():
    static_questions_data = Question.query.filter_by(type="static").all()
    static_questions = [q.question for q in static_questions_data]
    custom_questions_data = Question.query.filter_by(type="custom").all()
    custom_questions = [q.question for q in custom_questions_data]

    return render_template('index.html',
                           static_questions=static_questions,
                           custom_questions=custom_questions)

@app.route('/add', methods=['POST'])
def add():
    custom_question = request.form['q']
    db.session.add(Question(custom_question, "custom"))
    db.session.commit()

    return ('', 204) # Intentional empty response


if __name__ == '__main__':
    app.run()