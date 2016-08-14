from app import app, db
from models import Question

with app.app_context():
    db.create_all()

static_questions_text = [
    "Real Name: ",
    "What we should call you: ",
    "Alto or Tenor: ",
    "Hometown: ",
    "Birthday: ",
    "Northwestern Residence: ",
    "Cell Phone Number: ",
    "Year in School (or alumni): ",
    "School: ",
    "Intended Area of Study: ",
    "Unreasonable Dream Area of Study: ",
    "AIM Screenname: ",
    "T-shirt Size: ",
    "Food Allergies: ",
    "Preferred Term for Carbonated Beverages: ",
    "Favorite color: ",
    "Favorite number: ",
    "Favorite website: ",
    "Favorite key: ",
    "Favorite genre of music to play: ",
    "Favorite Type of Candy: ",
    "Favorite Pick-up line: ",
    "Least favorite day of the week: ",
    "Favorite song from HS Marching Band: ",
    "Instrument(s) you would admit to playing: ",
    "Neck strap color: ",
    "Reed strength/brand: ",
    "Song you want as your theme song: ",
    "Movie you want to watch right now: ",
    "\"Oh man, you guys totally need to check out this TV Show\": ",
    "Favorite YouTube video: ",
    "Favorite gif: ",
    "Summer Activities: ",
    "What you think \"Prime conspiracy Centaur aftertaste\" means: ",
    "Craziest Summer Moment: ",
    "Would you like to be a part of the Saxo Fantasy Football League: ",
    "Three Books you would bring on a Desert Island: ",
    "Hottest Female Celebrity: ",
    "Hottest Male Celebrity: ",
    "Favorite NU alumnus: ",
    "Please assemble a team of 4 Badass Characters to help an old woman across the street: ",
    "Please propose a dress-up day theme for your section (On Thursday night rehearsals, each section dresses up in a certain theme): "
]

with app.app_context():
    for question in static_questions_text:
        db.session.add(Question(question, "static"))

    db.session.commit()


# As of 8/11/2016
custom_questions_text = [
    "Do you play Pokemon Go, why or why not? ",
    "favorite existentialist philosopher ",
    "Who is your favorite Jonas Brother? ",
    "Favorite Olympic sport to watch? ",
    "Favorite animal and why? ",
    "Favorite Pokemon? ",
    "What instrument(s) would you like to learn how to play? ",
    "If you could make one vintage meme popular again, what would you bring back? ",
    "Which Olympic event would you want to compete in? ",
    "Favorite Spongebob quote. ",
    "game you're most hyped for this season? ",
    "emacs or vim? ",
    "Mac or PC? ",
    "Or nah?? ",
    "What would you say is the real breakfast of champions? ",
    "Favorite dog breed? "
]

with app.app_context():
    for question in custom_questions_text:
        db.session.add(Question(question, "custom"))

    db.session.commit()
