from website.blog import bp
import html
from flask import render_template



@bp.context_processor
def get_thumbnail():
    def _get_thumbnail(google_url):
        link = google_url.split('=',1)[0]+"=w100"
        return link
    return dict(get_thumbnail=_get_thumbnail)


@bp.context_processor
def get_inline():
    def _get_inline(google_url):
        link = google_url.split('=',1)[0]+"=w480"
        return link
    return dict(get_inline=_get_inline)


@bp.context_processor
def gallery_item():
    def _gallery_item(gallery_item={}):
        gallery_item["inline_link"]=\
            gallery_item["google_url"].split('=',1)[0]+"=w550"

        rv=render_template(
            "galleries/gallery_img.html", item=gallery_item)
        return rv
    return dict(gallery_item=_gallery_item)


@bp.context_processor
def gallery():
    def _gallery(gal={}):
        rv=render_template(
            "galleries/gallery.html", gal=gal)
        return rv
    return dict(gallery=_gallery)


@bp.context_processor
def recipe():
    def _recipe(details={}):
        return render_template('recipe.html', details=details)
    return dict(recipe=_recipe)