from app import app
from flask import render_template

@app.route('/')
def home():
    posts = [
        {
            'first_name': 'Derek', 
            'last_name': 'Hawkins', 
            'body': 'This is the first post',
            'date_posted': 9
        },
        {
            'first_name': 'Lucas', 
            'last_name': 'Lang', 
            'body': 'This is the second post',
            'date_posted': 10
        },
        {
            'first_name': 'Ripal', 
            'last_name': 'Patel', 
            'body': 'This is the third post',
            'date_posted': 6
        }
    ]

    context = {
        'posts': posts
    }
    # return render_template('home.html', body='This is the first post', first_name='Derek', last_name='Lang', date_posted=9)
    return render_template('home.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')