CREATE TABLE IF NOT EXISTS customer_table(
    TableId INT PRIMARY KEY,
    Seats INT,
    Available BOOLEAN,
    EstimatedWaiting TIME,
    Fk_UserId INT,
    FOREIGN KEY (Fk_UserId) REFERENCES User(UserId)
);

CREATE TABLE IF NOT EXISTS User(
    UserId INT PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    UserPassword VARCHAR(100) NOT NULL,
    Fk_Table_Id INT,
    Fk_OrderID INT,
    permission VARCHAR(100),
    FOREIGN KEY (Fk_Table_Id) REFERENCES customer_table(TableId),
    FOREIGN KEY (Fk_OrderId) REFERENCES Orders(OrderId)
);

CREATE TABLE IF NOT EXISTS Orders(
    OrderId INT PRIMARY KEY,
    OrderDate TIME,
    PickupDate TIME,
    Quantity INT,
    FoodId INT,
    UnitPrice PRECISION DECIMAL(6,2),
    Fk_UserId INT,
    Fk_TableId INT,
    FOREIGN KEY (Fk_UserId) REFERENCES User(UserId),
    FOREIGN KEY (FoodId) REFERENCES FoodItem(FoodId),
    FOREIGN KEY (Fk_TableId) REFERENCES customer_table(TableId)
);

CREATE TABLE IF NOT EXISTS FoodItem(
    FoodId INT PRIMARY KEY,
    FoodName VARCHAR(100),
    Quantity INT,
    UnitPrice PRECISION DECIMAL(6,2),
    ItemCategory VARCHAR(100),
    GlutenFree BOOLEAN,
    ContainsMeat BOOLEAN,
    Vegan BOOLEAN
);

CREATE TABLE IF NOT EXISTS Menu(
    MenuID INT PRIMARY KEY,
    Price PRECISION DECIMAL(6,2),
    StartDate DATE,
    EndDate DATE,
    Fk_FoodId VARCHAR(100),
    Fk_OrderId INT,
    FOREIGN KEY (Fk_OrderId) REFERENCES Orders(OrderId),
    FOREIGN KEY (fK_FoodId) REFERENCES FoodItem(FoodId)
);

CREATE TABLE IF NOT EXISTS Reviews(
    reviewID INT PRIMARY KEY,
    timeReview Date,
    starReview INT,
    Fk_UserId INT,
    Fk_MenuId INT,
    Fk_FoodId INT,
    FOREIGN KEY (Fk_UserId) REFERENCES User(UserId),
    FOREIGN KEY (Fk_MenuId) REFERENCES Menu(MenuID),
    FOREIGN KEY (Fk_FoodId) REFERENCES FoodItem(FoodId)
);



