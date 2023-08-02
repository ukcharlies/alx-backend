#!/usr/bin/env python3
"""Flask app."""
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    """View function for root route

    Returns:
        html: homepage
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
