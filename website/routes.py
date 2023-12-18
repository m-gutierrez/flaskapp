from flask import render_template, redirect, url_for
from flask_login import current_user
from website import app

@app.route('/')
def home():
    return render_template('home.html', user=current_user, posts={})


@app.route('/about')
def about():
    return render_template('about.html', user=current_user, posts={})
