import os
from flask import Flask, render_template_string
from flask_flatpages import pygmented_markdown
import markdown

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def my_renderer(text, fp, page):
    prerendered_body = render_template_string(text, page=page)
    return pygmented_markdown(prerendered_body)



class Config:

    PREFERRED_URL_SCHEME = 'https'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'blog_test.db')

    SECRET_KEY = 'you-will-never-guess'
    
    FLATPAGES_ROOT='blog/posts'
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_HTML_RENDERER = my_renderer
    FLATPAGES_MARKDOWN_EXTENSIONS= ['fenced_code']
    FLATPAGES_EXTENSION_CONFIGS = {
        'codehilite': {
            'linenums': 'True'
        }
    }


    GOOGLE_SCOPE = ['email', 'profile']
    GOOGLE_OAUTH_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID", None)
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration")
    OAUTHLIB_RELAX_TOKEN_SCOPE = True
