CREATE TABLE IF NOT EXISTS Person(
    User_ID INT PRIMARY KEY,
    email VARCHAR(100),
    password VARCHAR(100),
    permission VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Orders(
    Order_ID INT PRIMARY KEY,
    Fk_User_ID INT,
    Fk_Table_ID INT,
    FOREIGN KEY (Fk_User_ID) REFERENCES Person(User_ID),
    FOREIGN KEY (Fk_Table_ID) REFERENCES customer_table(tableID)
);

CREATE TABLE IF NOT EXISTS Menu(
    Menu_ID INT PRIMARY KEY,
    Menu_Item_ID INTEGER,
    Fk_Order_ID INT,
    FOREIGN KEY (Fk_Order_ID) REFERENCES Orders(Order_ID)
);

CREATE TABLE IF NOT EXISTS customer_table(
    tableID INT PRIMARY KEY,
    Fk_User_ID INT,
    FOREIGN KEY (Fk_User_ID) REFERENCES Person(User_ID)
);

CREATE TABLE IF NOT EXISTS Reviews(
    reviewID INT PRIMARY KEY,
    timeReview Date,
    starReview INT,
  	Fk_User_id INT,
  	FOREIGN KEY (Fk_User_ID) REFERENCES Person(User_ID)
);