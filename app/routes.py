from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'jamie'}
    posts = [
        {
            'author': {'username': 'jamie1'},
            'body': 'test1'
        },
        {
            'author': {'username': 'jamie2'},
            'body': 'test2'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
