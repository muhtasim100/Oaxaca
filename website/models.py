from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Person(db.Model):
    __tablename__ = 'Customer'
    UserId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=True)
    Email = db.Column(db.String(100),nullable=True, unique=True)
    Password = db.Column(db.String(100),nullable=True)
    Status = db.Column(db.String(100))
    PaymentId = db.Column(db.String(100),nullable=True, unique=True)
    Fk_OrderId = db.Column(db.Integer, db.ForeignKey('Orders.OrderId'))
    def get_UserId(self):
        return self.UserId
    def set_UserId(self, UserId):
        self.UserId = UserId
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
    def get_PaymentId(self):
        return self.PaymentId
    def set_PaymentId(self, PaymentId):
        self.PaymentId = PaymentId

class customer_table(db.Model):
    __tablename__ = 'customer_table'
    TableId = db.Column(db.Integer, primary_key=True)
    Seats = db.Column(db.Integer)
    Availability = db.Column(db.Boolean)
    EstimatedWaiting = db.Column(db.Time)
    Fk_UserId = db.Column(db.Integer, db.ForeignKey('Person.UserId'))


class Staff(db.Model):
    __tablename__ = 'Staff'
    StaffId = db.Column(db.Integer, primary_key=True)
    Fk_Table_Id = db.Column(db.Integer, db.ForeignKey('customer_table.TableId'))
    Fk_OrderID = db.Column(db.Integer, db.ForeignKey('Orders.OrderId'))
    PaymentDate = db.Column(db.Date)
    permission = db.Column(db.String(100))
    Amount = db.Column(db.DECIMAL(6,2))
    PaymentType = db.Column(db.String(100))


class Orders(db.Model):
    __tablename__ = 'Orders'
    OrderId = db.Column(db.Integer, primary_key=True)
    OrderDate = db.Column(db.Time)
    PickupDate = db.Column(db.Time)
    Quantity = db.Column(db.Integer)
    UnitPrice = db.Column(db.DECIMAL(6,2))
    FoodId = db.Column(db.Integer, db.ForeignKey('FoodItem.FoodId'))
    Fk_UserId = db.Column(db.Integer, db.ForeignKey('Person.UserId'))
    Fk_TableId = db.Column(db.Integer, db.ForeignKey('customer_table.TableId'))


class Menu(db.Model):
    __tablename__ = 'Menu'
    MenuID = db.Column(db.Integer, primary_key=True)
    Price = db.Column(db.DECIMAL(6,2))
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    FK_FoodId = db.Column(db.String(100), db.ForeignKey('FoodItem.FoodId'))
    Fk_OrderId = db.Column(db.Integer, db.ForeignKey('Orders.OrderId'))

class FoodItem(db.Model):
    __tablename__ = 'FoodItem'
    FoodId = db.Column(db.Integer, primary_key=True)
    FoodName = db.Column(db.String(100))
    Quantity = db.Column(db.Integer)
    UnitPrice = db.Column(db.DECIMAL(6,2))
    ItemCategory = db.Column(db.String(100))
    GlutenFree = db.Column(db.Boolean)
    ContainsMeat = db.Column(db.Boolean)
    Vegan = db.Column(db.Boolean)

class Reviews(db.Model):
    __tablename__ = 'Reviews'
    reviewID = db.Column(db.Integer, primary_key=True)
    timeReview = db.Column(db.Date)
    starReview = db.Column(db.Integer)
    Fk_UserId = db.Column(db.Integer, db.ForeignKey('Person.UserId'))
    Fk_MenuId = db.Column(db.Integer, db.ForeignKey('Menu.MenuId'))
    Fk_FoodId = db.Column(db.Integer, db.ForeignKey('FoodItem.FoodId'))