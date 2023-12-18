from flask import render_template
from flask import redirect
from flask import url_for
from website import pages
import os
import json
from flask_login import current_user
from website.models import AUTH
from flask_flatpages import pygments_style_defs
from website.blog import bp


@bp.route('/home')
def home():
    print(pages.root)
    post_filenames = os.listdir(
        os.path.join(pages.root))

    posts = [pages.get(path.rstrip('.md')) for path in post_filenames]
    posts = sorted(posts, key=lambda x: x.meta["date"], reverse=True)

    return render_template(
        'blog/blog.html', title='blog', user=current_user, posts=posts)


@bp.route('/<name>')
def post(name):
    post = pages.get_or_404(name)
    post_permission = post.meta.get('permissions')
    if post_permission:
        permission = AUTH[post_permission.upper()]
    else:
        permission = AUTH.PUBLIC

    if permission is AUTH.PUBLIC:
        print('public entering')
        return render_template(
            "blog/post.html", page=post, user=current_user, posts={})
    elif current_user.is_anonymous:
        print('anonymous entering')

        return redirect(url_for("blog.access_denied"))
    elif current_user.auth.value >= permission.value:
        return redirect(url_for("blog.access_denied"))
    else:
        return render_template(
            "blog/post.html", page=post, user=current_user, posts={})


@bp.route('/access_denied')
def access_denied():
    return render_template('blog/access_denied.html', user=current_user, posts={} )


@bp.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}