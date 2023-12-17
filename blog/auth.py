from flask import render_template, request, redirect, url_for
import requests
from blog import app, client, Config, login_manager, db
import os
from blog.models import AUTH, User, LogIns
import json
from flask_login import (
        current_user,
        login_required,
        login_user,
        logout_user,
        UserMixin
)


# class User(UserMixin):
#     def __init__(self, id_, name, email, profile_pic, auth):
#         self.id = id_
#         self.name = name
#         self.email = email
#         self.profile_pic = profile_pic
#         self.auth = auth

#     @staticmethod
#     def get(user_id):
#         if user_id in USER:
#             return USER[user_id]
#         else:
#             return None


# USER = {"1": User(1, 'test', 'email', 'pic', AUTH.PUBLIC)}


@login_manager.user_loader
def load_user(id):
    return User.get(id)

@app.route('/login')
def login():
    # find out what url to hit for google login
    google_provider_cfg = requests.get(
        Config.GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # use library to construct the request for google login and provide
    # scopes that let you retreive users profile from google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=f'{request.base_url}/callback',
        scope=["openid", "email", "profile"])

    return render_template(
        'login.html', user=current_user, posts={}, login_uri=request_uri)


@app.route('/login_link')
def login_link():
    # find out what url to hit for google login
    google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # use library to construct the request for google login and provide
    # scopes that let you retreive users profile from google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=f'{request.base_url}/callback',
        scope=["openid", "email", "profile"])

    return request_uri


@app.route("/login/callback")
def login_callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code
    )

    token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(Config.GOOGLE_OAUTH_CLIENT_ID, 
                Config.GOOGLE_OAUTH_CLIENT_SECRET))

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    print(userinfo_response.json())
    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    # by Google

    user = User(
        id=unique_id,
        username=users_name,
        email=users_email,
        picture=picture,
        auth=AUTH.PUBLIC
    )
    sign_in(user)
    # Begin user session by logging the user in
    login_user(user)

    print(user)
    # Send user back to homepage
    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))



def sign_in(user):

    dbuser = User.get(user.id)
    if dbuser:
        print('User exists, updating db')
        dbuser.username=user.username
        dbuser.email = user.email
        dbuser.picture = user.picture
    else:
        print('New user, adding to db')
        db.session.add(user)
    login = LogIns(user_id=user.id)
    db.session.add(login)
    db.session.commit()
