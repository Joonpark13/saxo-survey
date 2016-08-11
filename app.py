from flask import Flask, render_template
from socket import gethostname # For checking if it's running on pythonanywhere

app = Flask(__name__)
#TODO
# Currently just checks to see if app is running on pythonanywhere (intended
# quick deploy location) and turns debug on if not true. Later refactor for
# more robust deployment options.
if 'liveconsole' not in gethostname():
    app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html')