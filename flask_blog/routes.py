from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.form import LoginForm, RegistrationForm
from flask_blog.models import User, Post

posts = [

    {
        "author": "Watcharapong Wong",
        "title": "title1",
        "content": "The first post content",
        "date_posted": "April 20, 2021"
    },
    {
        "author": "Fread Frienstone",
        "title": "title2",
        "content": "The second post content",
        "date_posted": "April 21, 2021"
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account create for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"You have been logedin!", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Login Unsucessful. Please check username and password", "danger")
    return render_template('login.html', title='Login', form=form)