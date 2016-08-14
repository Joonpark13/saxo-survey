import os
from collections import OrderedDict

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
    static_data = user_data['static'] # Format: {"question_text1": "answer_text1", ...}
    custom_data = user_data['custom'] # Format: {"q": "question_text_here", "a": "answer_text_here"}

    db.session.add(Question(custom_data['q'], "custom"))

    combined_data = {} # Format: { id1: ["question_id1", "answer1"], ... }
    # Format static questions for storage
    for q in static_data:
        q_id = Question.query.filter_by(question=q).first().id
        combined_data[q_id] = static_data[q]
    # Format custom question for storage
    q_id = Question.query.filter_by(question=custom_data["q"]).first().id
    combined_data[q_id] = custom_data["a"]

    user = User(static_data['Real Name: '], combined_data)
    db.session.add(user)

    db.session.commit()

    return ('', 204) # Intentional empty response

@app.route('/results')
def results():
    user_data = User.query.all()
    for user in user_data:
        dataset = user.data # Format: { id1: "answer1", ... }
        # Convert question id to int
        converted_dataset = [(int(x[0]), x[1]) for x in dataset.items()] # x is the tuple
        user.data = OrderedDict(sorted(converted_dataset))
        # Replace question id with question text
        replaced_dataset = [(Question.query.get(x[0]).question, x[1]) for x in user.data.items()] # x is the tuple
        user.data = OrderedDict(replaced_dataset)

    return render_template('results.html', user_data=user_data)


if __name__ == '__main__':
    app.run()