from flask import render_template
from flask_login import current_user
from website.main import bp

@bp.route('/')
@bp.route('/home')
def home():
    return render_template(
        'home.html', title='Home', user=current_user, posts={})


@bp.route('/about')
def about():
    return render_template(
        'about.html', title='About', user=current_user, posts={})
