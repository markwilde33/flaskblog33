import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a1d4736cc4cf77c9188a1006f9432ea7'

posts = [
    {
        'author': 'Dr Hannibal Lecter',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 30, 2018'
    },
    {
        'author': 'Clarice Starling',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 1, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You are in baby!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unlucky mate, wrong details', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
