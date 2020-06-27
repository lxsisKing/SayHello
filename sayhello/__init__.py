from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from sayhello.extensions import db

APP_NAME = 'sayhello'

app = Flask(APP_NAME)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db.app = app
db.init_app(app)

from sayhello import commands, view

if __name__ == '__main__':
    app.run()
