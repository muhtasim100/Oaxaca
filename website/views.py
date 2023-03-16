from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from . import db
from .models import *
from flask_login import current_user
from sqlalchemy import func

views = Blueprint('views', __name__)

@views.route('/testing')
def testing():
    #Table
    ListTable =  customer_table.query.all()

    if FoodItem.query.count() != 1:
        testTable = customer_table(Seats = 4, Available = False, Fk_UserID = 1)



    #Food Items
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

    #Order
    if Orders.query.count() != 1:
        total = 0
        testOrder = Orders(Quantity=2, Fk_UserID=1, Fk_TableID=1)
        db.session.add(testOrder)
        db.session.commit()

        # Create order items
        print(testOrder.OrderID)
        item1 = OrderItem(FoodID=1, Quantity=1, OrderID = testOrder.OrderID)
        item2 = OrderItem(FoodID=2, Quantity=1, OrderID = testOrder.OrderID)
        db.session.add(item1)
        db.session.add(item2)
        db.session.commit()

        # Generate price 
        allFoodOrdered = OrderItem.query.filter_by(OrderID = 1)
        print(allFoodOrdered)
        for i in allFoodOrdered:
            food = FoodItem.query.filter_by(FoodID = i.FoodID).first()
            total += food.UnitPrice * i.Quantity
        testOrder.UnitPrice = total
        db.session.commit()

        # Add order items to the order
        testOrder.items.append(item1)
        testOrder.items.append(item2)
        db.session.commit()

        # Add the order to the database
        db.session.add(testOrder)
        db.session.commit()



    if Notification.query.count() != 1:
        test1 = Notification(statusNotification = 1, typeNotification = 1, FK_OrderID = 1, FK_UserID = current_user.UserID)
        db.session.add(test1)
        db.session.commit()

    return("Done!")


@views.route('/base')
def base():
    return render_template("base.html")


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/table')
def tables():
    return render_template("tables.html")


@views.route('/menu')
def menu():
    ListAll = FoodItem.query.all()
    return render_template("menu.html", res= ListAll)


@views.route('/payment')
def payment():
    return render_template("payment.html")


@views.route('/notif')
def notification():
    ListAll = Notification.query.all()
    return render_template("notifcentre.html", res=ListAll)


@views.route('/staff')
def staff():
    return render_template("staff_management.html")


@views.route('/order_tracker')
def order():
    return render_template("order_tracker.html")


@views.route('/reviews')
def reviews():
    reviewsAll = Reviews.query.all()
    return render_template("reviews.html", res=reviewsAll)

@views.route('/feedback')
def feedback():
    return render_template("feedback.html")

#POST REQUEST FOR STORING REVIEW
@views.route('/review_store', methods=["POST"])
def review_store():
    stars = request.form.get("stars")
    review = request.form.get("review")
    review_row = Reviews(Fk_UserID=current_user.UserID, starReview=int(stars))
    db.session.add(review_row)
    db.session.commit()

    return "Success", 200