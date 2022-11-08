from flask import Flask, render_template, url_for

new = Flask(__name__)

@new.route('/')
def home():
    return render_template('home.html')

@new.route('/about')
def about():
    return render_template('about.html')

@new.route('/contact')
def contact():
    return render_template('contact.html')

@new.route('/team')
def team():
    return render_template('team.html')


@new.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    new.run(debug=True)