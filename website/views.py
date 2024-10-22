from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from . import db
from .models import *
from .graphs import *
from flask_login import current_user
from functools import wraps
from sqlalchemy import func
from werkzeug.security import generate_password_hash

views = Blueprint('views', __name__)

@views.route('/testing')
def testing():
    #Table
    if customer_table.query.count() != 4:
        testTable1 = customer_table(Seats = 4, Available = 1)
        testTable2 = customer_table(Seats = 2, Available = 2)
        testTable3 = customer_table(Seats = 5, Available = 3)
        testTable4 = customer_table(Seats = 6, Available = 1) 
        db.session.add(testTable1)
        db.session.add(testTable2)
        db.session.add(testTable3)
        db.session.add(testTable4)
        db.session.commit()


    #Food Items
    if FoodItem.query.count() != 6:
        test1 = FoodItem(FoodName = "Tacos",  UnitPrice = 8.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = True, Vegan = False, Cals = 458)
        test2 = FoodItem(FoodName = "Quesadillas", UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = True, ContainsMeat = False, Vegan = False, Cals = 378)
        test3 = FoodItem(FoodName = "Fajita", UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = True, Vegan = False, Cals = 378)
        test4 = FoodItem(FoodName = "Burrito", UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = True, Cals = 350)
        test5 = FoodItem(FoodName = "Pozole", UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = False, Cals = 503)
        test6 = FoodItem(FoodName = "Menudo", UnitPrice = 6.99, ItemCategory = "Main Courses", GlutenFree = False, ContainsMeat = False, Vegan = False, Cals = 500)
        db.session.add(test1)
        db.session.add(test2)
        db.session.add(test3)
        db.session.add(test4)
        db.session.add(test5)
        db.session.add(test6)
        db.session.commit()


    if User.query.count() != 3:
        new_user1 = User(UserName="Alan Alan", Email="alanalan@gmail.com",
                         UserPassword=generate_password_hash("testing123", method='sha256'), Permission="Waiter")
        
        new_user2 = User(UserName="Bob Bob", Email="bobbob@gmail.com",
                         UserPassword=generate_password_hash("testing123", method='sha256'), Permission="Chef")
        
        new_user3 = User(UserName="Charlie Charlie", Email="charliecharlie@gmail.com",
                         UserPassword=generate_password_hash("testing123", method='sha256'), Permission="Owner")
        

        db.session.add(new_user1)
        db.session.add(new_user2)
        db.session.add(new_user3)
        db.session.commit()

    return("Done!")


@views.route('/base')
def base():
    return render_template("base.html", cart_products=cart_products(), notif_count=notif_count())


@views.route('/')
def home():
    x = db.session.query(Notification.typeNotification)
    return render_template("home.html", x=x, cart_products=cart_products(), notif_count=notif_count())


@views.route('/table')
def tables():
    ListAll =  customer_table.query.all()
    popups = {"add-table-popup": "+", "table-popup": "?"}
    return render_template("tables.html", res=ListAll, popups=popups, cart_products=cart_products(), notif_count=notif_count())


@views.route('/prod')
def product():
    ListAll = FoodItem.query.all()
    popups = {"add-dish-popup": "+", "allergy-popup": "?"}
    return render_template("Foodeditui.html", res= ListAll, popups=popups, cart_products=cart_products(), notif_count=notif_count())


@views.route('/menu')
def menu():
    ListAll = FoodItem.query.all()
    popups = {"add-dish-popup": "+", "allergy-popup": "?"}
    return render_template("menu.html", res= ListAll, popups=popups, cart_products=cart_products(), notif_count=notif_count())


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

    return render_template("payment.html", vat=vat_string, total_pounds=total_pounds, total_pence=total_pence, cart_products=cart_products(), notif_count=notif_count())


@views.route('/notif')
def notification():
    # OrderID, Total Price
    # Individual products: name, quantity, price
    ListAll = Notification.query.all()
    totalString = "N/A"
    totalPrice = 0
    products = {}

    for notif in ListAll:
        if notif.FK_OrderID != None:
            NotificationID = notif.NotificationID
            products[NotificationID] = []
            order = Orders.query.filter_by(OrderID=notif.FK_OrderID).first()
            totalPrice = order.UnitPrice
            order_items = OrderItem.query.filter_by(OrderID=notif.FK_OrderID)
            for item in order_items:
                food = FoodItem.query.filter_by(FoodID=item.FoodID).first()
                totalPrice += food.UnitPrice * item.Quantity
                products[notif.NotificationID].append(f"{item.Quantity}x {food.FoodName} (£{food.UnitPrice * item.Quantity:.2f})")
    
    totalString = f"£{totalPrice:.2f}"

    popups = {"order-popup": "?"}

    return render_template("notifcentre.html", res=ListAll, totalString=totalString, products=products, popups=popups, notif_count=notif_count())


@views.route('/staff')
def staff():
    return render_template("staff_management.html", notif_count=notif_count())


@views.route('/order_tracker/<int:order_id>')
def order(order_id):
    notif = Notification.query.filter_by(FK_OrderID=order_id).first()
    return render_template("order_tracker.html", order_id=order_id, status=notif.statusNotification)


@views.route('/order_tracker_staff/<int:order_id>')
def order_staff(order_id):
    notif = Notification.query.filter_by(FK_OrderID=order_id).first()
    totalString = "N/A"
    totalPrice = 0

    productList = []
    order = Orders.query.filter_by(OrderID=notif.FK_OrderID).first()
    totalPrice = order.UnitPrice
    order_items = OrderItem.query.filter_by(OrderID=notif.FK_OrderID)
    for item in order_items:
        food = FoodItem.query.filter_by(FoodID=item.FoodID).first()
        totalPrice += food.UnitPrice * item.Quantity
        productList.append(f"{item.Quantity}x {food.FoodName} (£{food.UnitPrice * item.Quantity:.2f})")

    totalString = f"£{totalPrice:.2f}"
    return render_template("order_tracker_staff.html", order_id=order_id, status=notif.statusNotification, totalString=totalString, productList=productList, notif_count=notif_count())


@views.route('/feedback')
def feedback():

    # Average Star Review
    avg_stars = "N / A"
    result = db.session.execute("SELECT AVG(starReview) FROM Reviews;")
    for row in result: # There's only one row
        if row[0] != None:
            avg_stars = f"{row[0]:.1f}"


    # List of Reviews
    reviews = db.session.execute("SELECT User.UserName, Reviews.starReview, Reviews.timeReview, Reviews.reviewID, Reviews.textReview " + 
        "FROM Reviews LEFT JOIN User ON Reviews.Fk_UserID = User.UserID " +
        "ORDER BY Reviews.timeReview DESC;")

    return render_template("feedback.html", avg_stars=avg_stars, dishes_graph=dishes_graph(), reviews=reviews, notif_count=notif_count())


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
  return "Success", 200


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

#POST REQUEST FOR DELETING NOTIFICATION FROM DB
@views.route('/delete_review', methods=["POST"])
def delete_review():
    RevID = int(request.form.get("id"))
    rev = Reviews.query.filter_by(reviewID=RevID).first()
    if rev:
        db.session.delete(rev)
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


#Helper function to get number of notifications
def notif_count():
    return Notification.query.count()


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
        order_item = OrderItem(FoodID=food_item.FoodID, Quantity=item.Quantity, OrderID=newOrder.OrderID)
        db.session.add(order_item)
        newOrder.items.append(order_item)

        #Update total price
        total += food_item.UnitPrice * item.Quantity

        #Delete from cart
        db.session.delete(item)

    newOrder.UnitPrice = total
    db.session.commit()

    # Add notification of the order to the database
    newNotif = Notification(statusNotification=1, typeNotification=1, FK_OrderID=newOrder.OrderID, FK_UserID=current_user.UserID)
    db.session.add(newNotif)
    db.session.commit()


    return str(newOrder.OrderID), 200


# Update the order status in notification
@views.route('/update_status', methods=["POST"])
def update_status():
    order_id = int(request.form.get("id"))
    order = Notification.query.filter_by(FK_OrderID=order_id).first()

    order.statusNotification += 1
    if (order.statusNotification > 3):
        order.statusNotification -= 3

    db.session.commit()

    return "Success", 200


#Post request to get products in menu
@views.route("/product_list", methods=["POST"])
def product_list():
    ListAll = FoodItem.query.all()
    filter_by = request.form.get("filter")

    if filter_by == "show_all":
        return render_template("all_menu.html", res=ListAll), 200
    
    elif filter_by == "gluten_menu":
        return render_template("gluten_menu.html", res=ListAll), 200
    
    elif filter_by == "meat_menu":
        return render_template("meat_menu.html", res=ListAll), 200

    elif filter_by == "vegan_menu":
        return render_template("vegan_menu.html", res=ListAll), 200


#Post request to add dish to menu
@views.route("/add_dish", methods=["POST"])
def add_dish():
    cd = {"on": True, None: False}
    dish_name = request.form.get("dish_name")
    dish_price = float(request.form.get("dish_price"))
    meat = cd[request.form.get("meat")]
    gluten = cd[request.form.get("gluten")]
    vegan = cd[request.form.get("vegan")]

    food = FoodItem(FoodName=dish_name, UnitPrice=dish_price, ItemCategory = "Main Courses", GlutenFree=gluten, ContainsMeat=meat, Vegan=vegan, Cals = 458)
    db.session.add(food)
    db.session.commit()

    return "Success", 200

#MISC
@views.route("/mockup")
def mockup():
    return redirect("https://www.figma.com/file/KiOG0Dcv57A8ykypouWFSA/Oaxaca?node-id=41-2&t=fdxUBKWSlkBZC2Wi-0")


@views.route("/trello")
def trello():
    return redirect("https://trello.com/b/OG2F31ch/sprint-5-13-03-2023")
