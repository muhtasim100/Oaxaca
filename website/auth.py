from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        flash('Already logged in, please sign out first!', category='error')
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.UserPassword, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Email or Password incorrect!', category='error')
        else:
            flash('Email or Password incorrect!', category='error')

    return render_template("login.html", user=current_user)    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        #Checking if the email is already in the database
        user = User.query.filter_by(Email=email).first()
        if user:
            flash('Account already exists.', category='error')

        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')

        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')

        else:
            new_user = User(UserName=name, Email=email, UserPassword=generate_password_hash(
                password, method='sha256'), Permission="Customer")

            db.session.add(new_user)
            db.session.commit()
            flash('Account created, please sign in!', category='success')

    return redirect(url_for('auth.login'))
