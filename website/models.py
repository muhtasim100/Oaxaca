from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(100), nullable=True)
    Email = db.Column(db.String(100), nullable=True, unique=True)
    UserPassword = db.Column(db.String(100), nullable=True)
    Status = db.Column(db.String(100))
    PaymentID = db.Column(db.String(100), nullable=True, unique=True)
    Fk_Table_ID = db.Column(db.Integer, db.ForeignKey('customer_table.TableID'))
    Fk_OrderID = db.Column(db.Integer, db.ForeignKey('Orders.OrderID'))
    Permission = db.Column(db.String(100))
    
    # Permissions:
        # Customer
        # Waiter
        # Chef
        # Owner

    def get_id(self):
        return self.UserID
        
    def get_UserID(self):
        return self.UserID

    def set_UserID(self, UserID):
        self.UserID = UserID

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    def get_Email(self):
        return self.Email

    def set_Email(self, Email):
        self.Email = Email

    def get_Password(self):
        return self.Password

    def set_Password(self, Password):
        self.Password = Password

    def get_Status(self):
        return self.Status

    def set_Status(self, Status):
        self.Status = Status

    def get_PaymentID(self):
        return self.PaymentID

    def set_PaymentID(self, PaymentID):
        self.PaymentID = PaymentID


class customer_table(db.Model):
    __tablename__ = 'customer_table'
    TableID = db.Column(db.Integer, primary_key=True)
    Seats = db.Column(db.Integer)
    Available = db.Column(db.Integer)
    # 1 -> Available
    # 2 -> Reserved
    # 3 -> Occupied
    Fk_UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))


class Orders(db.Model):
    __tablename__ = 'Orders'
    OrderID = db.Column(db.Integer, primary_key=True)
    OrderDate = db.Column(db.DateTime (timezone = True), default = func.now())
    Quantity = db.Column(db.Integer)
    UnitPrice = db.Column(db.Float(precision=8, asdecimal = True))
    Fk_UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    Fk_TableID = db.Column(db.Integer, db.ForeignKey('customer_table.TableID'))
    Fk_WaiterID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    items = db.relationship('OrderItem', backref='order', lazy='dynamic')


class Menu(db.Model):
    __tablename__ = 'Menu'
    MenuID = db.Column(db.Integer, primary_key=True)
    Price = db.Column(db.Float(precision=8, asdecimal = True))
    StartDate = db.Column(db.DateTime (timezone = True), default = func.now())
    EndDate = db.Column(db.DateTime (timezone = True), default = func.now())
    FK_FoodID = db.Column(db.String(100), db.ForeignKey('FoodItem.FoodID'))
    Fk_OrderID = db.Column(db.Integer, db.ForeignKey('Orders.OrderID'))


class FoodItem(db.Model):
    __tablename__ = 'FoodItem'
    FoodID = db.Column(db.Integer, primary_key=True)
    FoodName = db.Column(db.String(100))
    Quantity = db.Column(db.Integer)
    UnitPrice = db.Column(db.Float(precision=8, asdecimal = True))
    ItemCategory = db.Column(db.String(100))
    GlutenFree = db.Column(db.Boolean)
    ContainsMeat = db.Column(db.Boolean)
    Vegan = db.Column(db.Boolean)
    Cals = db.Column(db.Integer)


class OrderItem(db.Model):
    __tablename__ = 'OrderItem'
    ItemID = db.Column(db.Integer, primary_key=True)
    FoodID = db.Column(db.Integer, db.ForeignKey('FoodItem.FoodID'))
    Quantity = db.Column(db.Integer)
    OrderID = db.Column(db.Integer, db.ForeignKey('Orders.OrderID'))


class Reviews(db.Model):
    __tablename__ = 'Reviews'
    reviewID = db.Column(db.Integer, primary_key=True)
    timeReview = db.Column(db.DateTime (timezone = True), default = func.now())
    starReview = db.Column(db.Integer)
    textReview = db.Column(db.String(100))
    Fk_UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    Fk_MenuID = db.Column(db.Integer, db.ForeignKey('Menu.MenuID'))
    Fk_FoodID = db.Column(db.Integer, db.ForeignKey('FoodItem.FoodID'))


class Cart(db.Model):
    __tablename__ = 'Cart'
    cartID = db.Column(db.Integer, primary_key=True)
    Fk_UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    Fk_FoodID = db.Column(db.Integer, db.ForeignKey('FoodItem.FoodID'))
    Quantity = db.Column(db.Integer)


class Notification(db.Model):
    __tablename__ = 'Notification'
    NotificationID = db.Column(db.Integer, primary_key=True)
    TimeNotifcation = db.Column(db.DateTime (timezone = True), default = func.now())
    statusNotification = db.Column(db.Integer)
    # 1 -> Processing
    # 2 -> Working on it
    # 3 -> At the table
    typeNotification = db.Column(db.Integer)
    # 1 -> Customer has ordered
    # 2 -> Customer has called the waiter
    # 3 -> Customer has left
    # 4 -> Chef has called the waiter
    
    FK_OrderID = db.Column(db.Integer, db.ForeignKey('User.Fk_OrderID'))
    FK_UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
