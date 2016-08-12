from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = "question"

    question = db.Column(db.String(), primary_key=True)
    type = db.Column(db.String())

    def __init__(self, question, type):
        self.question = question
        self.type = type

    def __repr__(self):
        return "<{0} question {1}>".format(self.type, self.question)


class User(db.Model):
    __tablename__ = "user"

    name = db.Column(db.String(), primary_key=True)
    answers = db.Column(JSON)

    def __init__(self, name, answers):
        self.name = name
        self.answers = answers

    def __repr__(self):
        return "<user {0}>".format(self.name)
