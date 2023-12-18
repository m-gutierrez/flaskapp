from flask import Flask
from flask_flatpages import FlatPages
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

# initialize the app with the extension
db = SQLAlchemy()
db.init_app(app)

# Flat pages for blog posts
pages = FlatPages()

pages.init_app(app)

# User session management setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view= 'auth.login'


from website.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from website.blog import bp as blog_bp
app.register_blueprint(blog_bp, url_prefix='/blog')




from website import routes, jinja_ext