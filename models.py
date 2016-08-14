from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    type = db.Column(db.String())

    def __init__(self, question, type):
        self.question = question
        self.type = type # Should be either "static" or "custom"

    def __repr__(self):
        return "<{0} question {1}>".format(self.type, self.question)


class User(db.Model):
    __tablename__ = "user"

    name = db.Column(db.String(), primary_key=True)
    data = db.Column(JSON) # Format: { id: "answer" }

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __repr__(self):
        return "<user {0}>".format(self.name)
