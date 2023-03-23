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
        testOrder = Orders(Fk_UserID=1, Fk_TableID=1)
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
        test1 = Notification(statusNotification = 1, typeNotification = 2, FK_OrderID = 1, FK_UserID = current_user.UserID)
        db.session.add(test1)
        db.session.commit()

    return("Done!")


@views.route('/base')
def base():
    return render_template("base.html", cart_products=cart_products())


@views.route('/')
def home():
    x = db.session.query(Notification.typeNotification)
    return render_template("home.html", x=x)


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
    cart = Cart.query.filter_by(Fk_UserID=current_user.UserID)
    cart_total = 0
    for item in cart:
        food_item = FoodItem.query.filter_by(FoodID=item.Fk_FoodID).first()
        cart_total += item.Quantity * food_item.UnitPrice

    cart_total = float(cart_total)
    vat = 0.2 * cart_total
    vat_string = f"£{vat:.2f}"
    cart_total += vat
    total_string = f"{cart_total:.2f}"
    total_pounds, total_pence = total_string.split(".")

    return render_template("payment.html", vat=vat_string, total_pounds=total_pounds, total_pence=total_pence)


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
    reviews = db.session.execute("SELECT User.UserName, Reviews.starReview, Reviews.timeReview, Reviews.reviewID " + 
        "FROM Reviews LEFT JOIN User ON Reviews.Fk_UserID = User.UserID " +
        "ORDER BY Reviews.timeReview DESC;")

    return render_template("feedback.html", avg_stars=avg_stars, dishes_graph=dishes_graph(), reviews=reviews)


## POST REQUESTS

#POST REQUEST FOR STORING REVIEW
@views.route('/review_store', methods=["POST"])
def review_store():
    stars = request.form.get("stars")
    review = request.form.get("review")
    review_row = Reviews(Fk_UserID=current_user.UserID, textReview=review, starReview=int(stars))
    db.session.add(review_row)
    db.session.commit()

    return "Success", 200


#POST REQUEST FOR ADDING A TABLE
@views.route("/add_table", methods=["POST"])
def add_table():
  seats = int(request.form.get("seats"))
  NewTable = customer_table(Seats = seats, Available = 1) 
  db.session.add(NewTable)
  db.session.commit()


#POST REQUEST FOR DELETING PRODUCT FROM DB
@views.route('/delete_product', methods=["POST"])
def delete_product():
    food_id = int(request.form.get("id"))
    food = FoodItem.query.filter_by(FoodID=food_id).first()
    db.session.delete(food)
    db.session.commit()

    return "Success", 200

#POST REQUEST FOR CALLING WAITER
@views.route('/call_waiter', methods=["POST"])
def call_waiter():
    notif = Notification(statusNotification = 1, typeNotification = 2, FK_UserID = current_user.UserID)
    db.session.add(notif)
    db.session.commit()

    return "Success", 200

#POST REQUEST FOR DELETING NOTIFICATION FROM DB
@views.route('/delete_notif', methods=["POST"])
def delete_notif():
    NotifID = int(request.form.get("id"))
    notification = Notification.query.filter_by(NotificationID=NotifID).first()
    if notification:
        db.session.delete(notification)
        db.session.commit()

    return "Success", 200

# Helper function to get the html for the products in cart
def cart_products():
    cart = Cart.query.filter_by(Fk_UserID=current_user.UserID)
    cart_items = {}
    cart_total = 0
    for item in cart:
        food_item = FoodItem.query.filter_by(FoodID=item.Fk_FoodID).first()
        cart_items[item.cartID] = f"{item.Quantity}x {food_item.FoodName} (£{item.Quantity * food_item.UnitPrice:.2f})"
        cart_total += item.Quantity * food_item.UnitPrice

    cart_total = float(cart_total)
    vat = 0.2 * cart_total
    vat_string = f"£{vat:.2f}"
    cart_total += vat
    total_string = f"{cart_total:.2f}"
    total_pounds, total_pence = total_string.split(".")

    return render_template("cart_products.html", cart_items=cart_items, vat=vat_string, total_pounds=total_pounds, total_pence=total_pence)

#Post request to get the html for the products in cart to refresh dynamically
@views.route('/cart_products', methods=["POST"])
def cart_products_post():
    return cart_products(), 200


# For the food items on menu to add to cart
@views.route('/add_cart', methods=["POST"])
def add_cart():
    food_id = int(request.form.get("id"))
    cart = Cart.query.filter_by(Fk_FoodID=food_id, Fk_UserID=current_user.UserID).first()
    if not cart:
        new_cart = Cart(Fk_UserID=current_user.UserID, Fk_FoodID=food_id, Quantity=1)
        db.session.add(new_cart)
        
    else:
        cart.Quantity += 1

    db.session.commit()
    return "Success", 200

# For the plus button on basket to increase quantity
@views.route('/add_cart_quantity', methods=["POST"])
def add_cart_quantity():
    cart_id = int(request.form.get("id"))
    cart = Cart.query.filter_by(cartID=cart_id).first()
    cart.Quantity += 1

    db.session.commit()

    return "Success", 200

# For the minus button on basket to reduce quantity
@views.route('/minus_cart_quantity', methods=["POST"])
def remove_cart_quantity():
    cart_id = int(request.form.get("id"))
    cart = Cart.query.filter_by(cartID=cart_id).first()
    if cart.Quantity == 1:
        db.session.delete(cart)
        
    else:
        cart.Quantity -= 1

    db.session.commit()

    return "Success", 200


#Creating order after payment
@views.route('/create_order', methods=["POST"])
def create_order():
    total = 0
    newOrder = Orders(Fk_UserID=current_user.UserID, Fk_TableID=current_user.Fk_Table_ID)
    db.session.add(newOrder)
    db.session.commit()

    cart = Cart.query.filter_by(Fk_UserID=current_user.UserID)
    for item in cart:
        food_item = FoodItem.query.filter_by(FoodID=item.Fk_FoodID).first()
        
        #Add order items to the order
        order_item = OrderItem(FoodID=food_item.FoodID, Quantity=food_item.Quantity, OrderID=newOrder.OrderID)
        db.session.add(order_item)
        newOrder.items.append(order_item)

        #Update total price
        total += food_item.UnitPrice * food_item.Quantity

        #Delete from cart
        db.session.delete(item)

    newOrder.UnitPrice = total
    db.session.commit()

    # Add notification of the order to the database
    newNotif = Notification(statusNotification=1, typeNotification=1, FK_OrderID=newOrder.OrderID, FK_UserID=current_user.UserID)
    db.session.add(newNotif)
    db.session.commit()


    return "Success", 200
