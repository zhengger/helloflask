# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask
from flask import url_for
from flask import redirect
# from flask_foo import Foo

app001 = Flask(__name__)

# the minimal Flask application
@app001.route('/')
def index():
    result = 10
    return f"<h1>Hello!!, World {url_for('index')}!</h1>"


# bind multiple URL for one view function
@app001.route('/hi/')
@app001.route('/hello')
def say_hello():
    """
    multiple app.route() decorators for same viewfunction
    :return:
    """
    return '<h1>Hello, Flask!</h1>'

@app001.route('/greet/<name>')
@app001.route('/greet', defaults={'name': 'Programmer'})
def greet(name):
    """
    dynamic route, URL variable default
    variable name in URL
    :param name:
    :return:
    """
    # redirect('/hello')
    return f'<h1>Hello, {name}!</h1>'


@app001.cli.command()
def hello():
    """
    custom flask cli command, remember to import click in beginning
    :return:
    """
    """Just say hello."""
    click.echo('Hello, Human!')
