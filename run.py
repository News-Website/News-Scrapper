# -*- coding: utf-8 -*-
"""file docstring"""
from flask import Flask, render_template
from india import INDIA
from USA import USA

APP = Flask(__name__)
APP.register_blueprint(INDIA)
APP.register_blueprint(USA)


@APP.route('/')
def home():
    """home function for index page."""
    return render_template('Home.html')


if __name__ == '__main__':
    APP.run(debug=True)
