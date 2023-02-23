from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from . import db
from .models import FoodItem

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/table')
def tables():
    return render_template("tables.html")

@views.route('/menu')
def menu():
    ListAll = FoodItem.query.all()

    if FoodItem.query.count() != 1:
        test1 = FoodItem(FoodName = "Tacos", Quantity = 1, UnitPrice = 8.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = True, Vegan = False, Cals = 458)
        db.session.add(test1)
        db.session.commit()
        
    return render_template("menu.html", res= ListAll)
    