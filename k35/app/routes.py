from flask import render_template, request, redirect, url_for, flash, session
from k35.app import app
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from k35.app.models import query_db, execute_db

@app.route("/")
@app.route("/home")
def home():
    posts = query_db("SELECT * FROM post")
    return render_template('index.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        try:
            execute_db("INSERT INTO user (username, email, password) VALUES (?, ?, ?)", (username, email, password))
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists', 'danger')
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = query_db("SELECT * FROM user WHERE email = ?", (email,), one=True)
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        execute_db("INSERT INTO post (title, content, user_id) VALUES (?, ?, ?)", (title, content, session['user_id']))
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html')
