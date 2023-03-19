from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from . import db
from .models import *
from .graphs import *
from flask_login import current_user
from sqlalchemy import func

views = Blueprint('views', __name__)

@views.route('/testing')
def testing():
    #Table
    ListTable =  customer_table.query.all()

    if customer_table.query.count() != 4:
        testTable1 = customer_table(Seats = 4, Available = 1, Fk_UserID = 1)
        testTable2 = customer_table(Seats = 2, Available = 2, Fk_UserID = 2)
        testTable3 = customer_table(Seats = 5, Available = 3, Fk_UserID = 4)
        testTable4 = customer_table(Seats = 6, Available = 1, Fk_UserID = 5) 
        db.session.add(testTable1)
        db.session.add(testTable2)
        db.session.add(testTable3)
        db.session.add(testTable4)
        db.session.commit()

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
    ListAll =  customer_table.query.all()
    return render_template("tables.html", res=ListAll)


@views.route('/prod')
def product():
    ListAll = FoodItem.query.all()
    return render_template("Foodeditui.html", res= ListAll)


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


@views.route('/feedback')
def feedback():

    # Average Star Review
    avg_stars = "N / A"
    result = db.session.execute("SELECT AVG(starReview) FROM Reviews;")
    for row in result: # There's only one row
        if row[0] != None:
            avg_stars = f"{row[0]:.1f}"


    # List of Reviews
    reviews = db.session.execute("SELECT User.UserName, Reviews.starReview, Reviews.timeReview " + 
    "FROM Reviews LEFT JOIN User ON Reviews.Fk_UserID = User.UserID;")

    return render_template("feedback.html", avg_stars=avg_stars, dishes_graph=dishes_graph(), reviews=reviews)


#POST REQUEST FOR STORING REVIEW
@views.route('/review_store', methods=["POST"])
def review_store():
    stars = request.form.get("stars")
    review = request.form.get("review")
    review_row = Reviews(Fk_UserID=current_user.UserID, textReview=review, starReview=int(stars))
    db.session.add(review_row)
    db.session.commit()

    return "Success", 200


@views.route('/delete_product', methods=["POST"])
def delete_product():
    food_id = int(request.form.get("id"))
    food = FoodItem.query.filter_by(FoodID=food_id).first()
    db.session.delete(food)
    db.session.commit()

    return "Success", 200
