
PRAGMA foreign_keys = ON;

CREATE TABLE Account(
	id				INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	name			TEXT NOT NULL,
	email			TEXT NOT NULL,
	username		TEXT NOT NULL,
	password		TEXT NOT NULL,
	accounttype		INTEGER NOT NULL
);

CREATE TABLE Admin(
    phonenumber		TEXT,
	accountid		INTEGER PRIMARY KEY UNIQUE,
    FOREIGN KEY(accountid) REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Volunteer(
    phonenumber		TEXT,
    availability    TEXT,
	accountid		INTEGER PRIMARY KEY UNIQUE,
    managerid       INTEGER,
    FOREIGN KEY(accountid) REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(managerid) REFERENCES Admin(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Client(
    income 		    INTEGER,
	accountid		INTEGER PRIMARY KEY UNIQUE,
    FOREIGN KEY(accountid) REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE DietaryRestrictions(
    accountid		INTEGER,
    dietaryrestriction TEXT NOT NULL,
    PRIMARY KEY(accountid,dietaryrestriction),
    FOREIGN KEY(accountid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Reasons(
    clientid		INTEGER,
    reason	        TEXT NOT NULL,
    PRIMARY KEY (clientid,reason),
    FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Appointment(
    id 		        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    time		    TEXT NOT NULL,
    volunteerid     INTEGER NOT NULL,
    clientid        INTEGER NOT NULL,
    FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Dependant(  
    clientid		INTEGER,
    name            TEXT NOT NULL,  
    relationship    TEXT NOT NULL,
    PRIMARY KEY (clientid,name),
    FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Foodbank(  
    address         TEXT PRIMARY KEY NOT NULL,
    phonenumber		TEXT NOT NULL,
    email           TEXT NOT NULL,
    hours           TEXT NOT NULL,
    funds           INTEGER NOT NULL
);

INSERT INTO Foodbank (address, phonenumber, email, hours, funds) VALUES ("251 MacEwan Student Centre 2500 University Drive NW Calgary", 4032206551, "foodbank@ucalgary.ca", "WEEKDAYS 0900-1700", 0);


CREATE TABLE MaxRequests(
    famSize         INTEGER PRIMARY KEY UNIQUE,
    fruits          INTEGER NOT NULL,
    vegetables      INTEGER NOT NULL,
    potatoBags      INTEGER NOT NULL,
    eggs            REAL NOT NULL,
    butter          INTEGER NOT NULL,
    groundBeef      INTEGER NOT NULL,
    wholeChicken    INTEGER NOT NULL,
    veggieFrozen    INTEGER NOT NULL,
    bread           INTEGER NOT NULL,
    cannedVeggie    INTEGER NOT NULL,
    cannedFruit     INTEGER NOT NULL,
    cannedSoup      INTEGER NOT NULL,
    cannedSeafood   INTEGER NOT NULL,
    cannedMeat      INTEGER NOT NULL
);

INSERT INTO MaxRequests (famSize,fruits, vegetables,  potatoBags, eggs, butter, groundBeef, wholeChicken, veggieFrozen, bread, cannedVeggie, cannedFruit, cannedSoup, cannedSeafood, cannedMeat) VALUES (1,4,3,1,0.5,1,1,1,2,1,1,1,4,2,1);
INSERT INTO MaxRequests (famSize,fruits, vegetables,  potatoBags, eggs, butter, groundBeef, wholeChicken, veggieFrozen, bread, cannedVeggie, cannedFruit, cannedSoup, cannedSeafood, cannedMeat) VALUES (2,6,6,2,0.5,1,1,1,2,2,2,2,5,2,1);
INSERT INTO MaxRequests (famSize,fruits, vegetables,  potatoBags, eggs, butter, groundBeef, wholeChicken, veggieFrozen, bread, cannedVeggie, cannedFruit, cannedSoup, cannedSeafood, cannedMeat) VALUES (3,12,8,2,1,1,1,2,2,2,4,4,6,3,2);
INSERT INTO MaxRequests (famSize,fruits, vegetables,  potatoBags, eggs, butter, groundBeef, wholeChicken, veggieFrozen, bread, cannedVeggie, cannedFruit, cannedSoup, cannedSeafood, cannedMeat) VALUES (4,16,10,3,2,1,2,1,2,3,6,6,7,4,3);

CREATE TABLE RequestForm(
    id 		        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    fruits          INTEGER NOT NULL,
    vegetables      INTEGER NOT NULL,
    potatoBags      INTEGER NOT NULL,
    eggs            INTEGER NOT NULL,
    butter          INTEGER NOT NULL,
    groundBeef      INTEGER NOT NULL,
    wholeChicken    INTEGER NOT NULL,
    veggieFrozen    INTEGER NOT NULL,
    bread           INTEGER NOT NULL,
    cannedVeggie    INTEGER NOT NULL,
    cannedFruit     INTEGER NOT NULL,
    cannedSoup      INTEGER NOT NULL,
    cannedSeafood   INTEGER NOT NULL,
    cannedMeat      INTEGER NOT NULL,
    clientid        INTEGER NOT NULL,
    volunteerid     INTEGER,
    date		    TEXT NOT NULL,
    FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Donor(
    id 		        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name		    TEXT,
    phonenumber		TEXT,
    email           TEXT
);

CREATE TABLE Supplier(
    name		    TEXT PRIMARY KEY NOT NULL,
    phonenumber		TEXT NOT NULL,
    email           TEXT NOT NULL
);

CREATE TABLE Contacts(
    adminid         INTEGER NOT NULL,
    suppliername    TEXT NOT NULL,
    PRIMARY KEY(adminid, suppliername),
    FOREIGN KEY(adminid) REFERENCES Admin(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(suppliername) REFERENCES Supplier(name) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Supplies(
    suppliername    TEXT NOT NULL,
    foodbarcode     INTEGER NOT NULL,
    PRIMARY KEY(suppliername, foodbarcode),
    FOREIGN KEY(suppliername) REFERENCES Supplier(name) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Donates(
    donorid         INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL,
    quantity        INTEGER NOT NULL,
    PRIMARY KEY(donorid, foodbarcode),
    FOREIGN KEY(donorid) REFERENCES Donor(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Takes(
    clientid        INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL,
    quantity        INTEGER NOT NULL,
    PRIMARY KEY(clientid, foodbarcode),
    FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Foodstore(
    refcode     INTEGER NOT NULL,
    foodname    TEXT NOT NULL,
    quantity    INTEGER NOT NULL,
    expirydate  TEXT NOT NULL,
    address     TEXT NOT NULL,
    PRIMARY KEY(refcode),
    FOREIGN KEY(address) REFERENCES Foodbank(address) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Account(name, email, username, password, accounttype) VALUES ("Administrator One", "csus@ucalgary.ca", "csus", "cpsc2018", 2);
INSERT INTO Admin (phonenumber, accountid) VALUES (4031111111,1);

INSERT INTO Account(name, email, username, password, accounttype) VALUES ("Rahmanta Nadhif", "ceo@nadramon.com", "nadramon", "12321", 0);
INSERT INTO Client (income, accountid) VALUES (350,2);
INSERT INTO Dependant (clientid,name,relationship) VALUES (2, "Alfath Zakir", "Husband");

INSERT INTO Account(name, email, username, password, accounttype) VALUES ("Shayne Mujuru", "shayne@ucalgary.ca", "east", "111111", 1);
INSERT INTO Volunteer (phonenumber,availability, accountid,managerid) VALUES (4032141115,"Monday Tuesday Wednesday Thursday Friday",3,1);

INSERT INTO Account(name, email, username, password, accounttype) VALUES ("tester", "test@ucalgary.ca", "hello", "there", 0);
INSERT INTO Client (income, accountid) VALUES (500,4);




INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (1,'fruit',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (2,'carrot',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (3,'potatobag',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (4,'eggDozen',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (5,'butter',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (6,'groundBeef',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (7,'chicken',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (8,'frozenVeg',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (9,'bread',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (10,'cannedVeg',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (11,'cannedFruit',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (12,'cannedSoup',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (13,'cannedSeafood',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");
INSERT INTO Foodstore(refcode,foodname,quantity,expirydate,address) VALUES (14,'cannedMeat',200,"10-20-2019","251 MacEwan Student Centre 2500 University Drive NW Calgary");