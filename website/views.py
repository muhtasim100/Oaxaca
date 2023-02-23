from flask import Blueprint, render_template, request, session, url_for, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/table')
def tables():
    return render_template("tables.html")

@views.route('/payment')
def payment():
    return render_template("payment.html")

@views.route('/notif')
def notification():
    return render_template("notifcentre.html")

@views.route('/staff')
def staff():
    return render_template("staff_management.html")
