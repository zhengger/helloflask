# code:utf-8
import os, sys, click
from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

"""
    db.Integer 整型
    db.String (size) 字符串，size 为最大长度，比如db.String(20)
    db.Text 长文本
    db.DateTime 时间日期，Pythondatetime对象
    db.Float 浮点数
    db.Boolean 布尔值
"""
@app.cli.command()
@click.option('--drop', is_flag=True, help='Creat after drop.')
def initdb(drop):
    """initialize the database
    
    Arguments:
        drop {[type]} -- [description]
    """
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized databse.')

@app.cli.command()
def forge():
    """Generate fake data.
    """
    name = 'Gray Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    
    db.session.commit()
    click.echo('Done.')


@app.route('/')
@app.route('/about')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    flash('Hello, World!')
    return render_template('index.html', name=user.name, movies=movies)


