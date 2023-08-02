 #!/usr/bin/env python3
"""Basic Babel Setup."""
from flask import Flask, render_template
from flask_babel import Babel


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
    """View function for root route

    Returns:
        html: homepage
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()