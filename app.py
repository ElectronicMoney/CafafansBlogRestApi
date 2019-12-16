from flask import Flask, render_template
import os

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    posts = [
                {
                'id': 1,
                'author': 'Emeka Augustine',
                'title': 'Nigerian is a corrupt country!',
                'body': 'Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.',
                'date_posted': 'December 15, 2019'
            },
            {
                'id': 2,
                'author': 'Ben James',
                'title': 'Ghana is a corrupt country!',
                'body': ' Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur  adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.',
                'date_posted': 'December 16, 2019'
            }
    ]

    return render_template('home.html', posts=posts)

# About Us
@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT')))