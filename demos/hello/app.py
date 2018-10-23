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
# from flask_foo import Foo

app = Flask(__name__)

# the minimal Flask application
@app.route('/')
def index():
    result = 10
    return f"<h1>Hello, World {url_for('index')}!</h1>"


# bind multiple URL for one view function
@app.route('/hi/')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
