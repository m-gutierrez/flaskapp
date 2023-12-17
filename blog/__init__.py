from flask import Flask
from flask_flatpages import FlatPages
from config import Config
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

# initialize the app with the extension
db = SQLAlchemy(app)

# Flat pages for blog posts
pages = FlatPages(app)


# User session management setup
login_manager = LoginManager()
login_manager.init_app(app)

# OAuth 2 client setup for google-sign-in
client = WebApplicationClient(Config.GOOGLE_OAUTH_CLIENT_ID)


from blog import routes, jinja_ext, auth