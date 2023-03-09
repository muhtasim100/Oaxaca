from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from . import db
from .models import FoodItem

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/prod')
def product():
    ListAll = FoodItem.query.all()

    if FoodItem.query.count() != 6:
        test1 = FoodItem(FoodName = "Tacos", Quantity = 1, UnitPrice = 8.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = True, Vegan = False, Cals = 458)
        test2 = FoodItem(FoodName = "Quesadillas", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = True, ContainsMeat = False, Vegan = False, Cals = 378)
        test3 = FoodItem(FoodName = "Fajita", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = True, Vegan = False, Cals = 378)
        test4 = FoodItem(FoodName = "Burrito", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = True, Cals = 350)
        test5 = FoodItem(FoodName = "Pozole", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = False, Cals = 503)
        test6 = FoodItem(FoodName = "Menudo", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = False, Cals = 500)
        db.session.add(test1)
        db.session.add(test2)
        db.session.add(test3)
        db.session.add(test4)
        db.session.add(test5)
        db.session.add(test6)
        db.session.commit()
        
    return render_template("Foodeditui.html", res= ListAll)

@views.route('/table')
def tables():
    return render_template("tables.html")

@views.route('/menu')
def menu():
    ListAll = FoodItem.query.all()

    if FoodItem.query.count() != 6:
        test1 = FoodItem(FoodName = "Tacos", Quantity = 1, UnitPrice = 8.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = True, Vegan = False, Cals = 458)
        test2 = FoodItem(FoodName = "Quesadillas", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = True, ContainsMeat = False, Vegan = False, Cals = 378)
        test3 = FoodItem(FoodName = "Fajita", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = True, Vegan = False, Cals = 378)
        test4 = FoodItem(FoodName = "Burrito", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = True, Cals = 350)
        test5 = FoodItem(FoodName = "Pozole", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = False, Cals = 503)
        test6 = FoodItem(FoodName = "Menudo", Quantity = 1, UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = False, Cals = 500)
        db.session.add(test1)
        db.session.add(test2)
        db.session.add(test3)
        db.session.add(test4)
        db.session.add(test5)
        db.session.add(test6)
        db.session.commit()
        
    return render_template("menu.html", res= ListAll)
    
@views.route('/payment')
def payment():
    return render_template("payment.html")

@views.route('/notif')
def notification():
    return render_template("notifcentre.html")

@views.route('/staff')
def staff():
    return render_template("staff_management.html")
