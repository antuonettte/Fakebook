from app import app
from flask import render_template
from app.models import Post

@app.route('/')
def home():
    context = {
        'posts': Post.query.all()
    }
    # return render_template('home.html', body='This is the first post', first_name='Derek', last_name='Lang', date_posted=9)
    return render_template('home.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')