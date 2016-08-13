import os

from flask import Flask, render_template, url_for, request
from models import db, Question, User


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
    user_data = request.get_json()
    static_data = user_data['static'] # format: {question_text1: answer_text1, ...}
    custom_data = user_data['custom'] # format: {q: question_text_here, a: answer_text_here}
    combined_data = static_data.copy()
    combined_data.update({custom_data['q']: custom_data['a']})

    db.session.add(Question(custom_data['q'], "custom"))

    user = User(static_data['Real Name: '], combined_data)
    db.session.add(user)

    db.session.commit()

    return ('', 204) # Intentional empty response

@app.route('/results')
def results():
    user_data = User.query.all()

    return render_template('results.html', user_data=user_data)


if __name__ == '__main__':
    app.run()