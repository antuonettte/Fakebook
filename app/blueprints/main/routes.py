from app.blueprints.main.models import Post
from app.blueprints.auth.models import User
from app.blueprints.main import db
from flask import render_template, request, redirect, url_for, flash, current_app as app
from flask_login import current_user
# from .import bp as app



@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        p = Post(
                body=request.form.get('body'),
                user_id=1
            )
        db.session.add(p)
        db.session.commit()
        flash('Post created successfully', 'success')

        return redirect(url_for('home'))

    context = {
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    # return render_template('home.html', body='This is the first post', first_name='Derek', last_name='Lang', date_posted=9)
    return render_template('home.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == 'POST':

        u = User()
        u.update_profile(request.form)

        flash('User has updated profile successfully!', 'success')
        redirect(url_for('profile'))

    return render_template('profile.html')