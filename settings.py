# http://stackoverflow.com/questions/14825787/flask-how-to-read-a-file-in-application-root
import os

# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')