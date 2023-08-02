#!/usr/bin/env python3
"""Babel Setup."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone as confirm_timezone
from pytz.exceptions import UnknownTimeZoneError

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for flask app
    """
    DEBUG = True
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """view function for root route

    Returns:
        html: homepage
    """
    return render_template('6-index.html')


# @babel.localeselector
def get_locale():
    """get best language match

    Returns:
        str: best match
    """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """get user from mock database

    Returns:
        dict: user dictionary or None if unsuccessful
    """
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """set user from get_user as a global
       on flask.g.user
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """get user timezone

    Returns:
        str: user timezone
    """
    try:
        if request.args.get("timezone"):
            zone = request.args.get('timezone')
            timezone = confirm_timezone(zone)

        elif g.user:
            zone = g.user.get('timezone')
            timezone = confirm_timezone(zone)

    except UnknownTimeZoneError():
        timezone = 'UTC'

    return timezone


# --- uncomment this method
# babel.init_app(
#     app,
#     locale_selector=get_locale,
#     timezone_selector=get_timezone
# )
# --- and comment the @babel.localeselector and
#                     @babel.timezoneselector decorators
# above if you get this error:
# AttributeError: 'Babel' object has no attribute 'localeselector' or
# AttributeError: 'Babel' object has no attribute 'timezoneselector

if __name__ == '__main__':
    app.run()
