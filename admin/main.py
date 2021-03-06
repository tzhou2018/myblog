from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = '/admin/login'
login_manager.init_app(app)
