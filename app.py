from flask import Flask, render_template, url_for, flash, redirect, request
import os
from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm

app = Flask(__name__)

# The Secre Key
app.config['SECRET_KEY'] = '9e1f397f99dd55cb22e2ee55400fcd26'

# Home Page
@app.route('/')
def home():
    posts = [
                {
                'id': 1,
                'author': 'Emeka Augustine',
                'title': 'Nigerian is a corrupt country!',
                'content': 'Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.',
                'date_posted': 'December 15, 2019'
            },
            {
                'id': 2,
                'author': 'Ben James',
                'title': 'Ghana is a corrupt country!',
                'content': ' Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur  adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.',
                'date_posted': 'December 16, 2019'
            }
    ]

    return render_template('home.html', posts=posts)

# About Us
@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        # Check if the request method is post
        if request.method == 'POST':
            if form.email.data == 'admin@cafafans.com' and form.password.data == 'password':
                flash(f'You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash(f'Invalid username or Password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        # Check if the form is validated
        if form.validate_on_submit():
            flash(f'Acount Created for User {form.username.data}!', 'success')
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT')))