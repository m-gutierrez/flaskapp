from flask import render_template, redirect, url_for
from blog import app, pages
import os
import json
from flask_login import current_user
from blog.models import AUTH
from flask_flatpages import pygments_style_defs


@app.route('/')
def home():
    return render_template('home.html', user=current_user, posts={})


@app.route('/about')
def about():
    return render_template('about.html', user=current_user, posts={})


@app.route('/blog')
def blog():
    post_filenames = os.listdir(os.path.join(app.root_path, pages.root))

    posts = [pages.get(path.rstrip('.md')) for path in post_filenames]
    posts = sorted(posts, key=lambda x: x.meta["date"], reverse=True)

    return render_template(
        'blog.html', title='blog', user=current_user, posts=posts)


@app.route('/blog/<name>')
def post(name):
    post = pages.get_or_404(name)
    if post.meta.get('permissions'):
        permission = AUTH[post.meta.get('permissions').upper()]
    else:
        permission = AUTH.PUBLIC

    if permission is AUTH.PUBLIC:
        print('public entering')
        return render_template(
            "post.html", page=post, user=current_user, posts={})
    elif current_user.is_anonymous:
        print('anonymous entering')

        return redirect(url_for("access_denied"))
    elif current_user.auth.value >= permission.value:
        return redirect(url_for("access_denied"))
    else:
        return render_template(
            "post.html", page=post, user=current_user, posts={})


@app.route('/access_denied')
def access_denied():
    return render_template('access_denied.html', user=current_user, posts={} )


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}