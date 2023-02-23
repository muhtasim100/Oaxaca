from flask import Blueprint, render_template, request, session, url_for, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/prod')
def product():
    return render_template("Foodeditui.html")