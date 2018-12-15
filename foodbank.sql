
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
	accountid		INTEGER PRIMARY KEY UNIQUE REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Volunteer(
    phonenumber		TEXT,
    availability    TEXT,
	accountid		INTEGER UNIQUE REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE,
    managerid       INTEGER REFERENCES Admin(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Client(
    income 		    INTEGER,
	accountid		INTEGER PRIMARY KEY UNIQUE REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE
);


--done
CREATE TABLE DietaryRestrictions(
    accountid		INTEGER REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    dietaryrestriction TEXT NOT NULL,
    PRIMARY KEY (accountid,dietaryrestriction)
);

--done
CREATE TABLE Reasons(
    clientid		INTEGER REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    reason	    TEXT NOT NULL,
    PRIMARY KEY (clientid,reason)
    -- FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Appointment(
    id 		        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    time		    TEXT NOT NULL,
    volunteerid     INTEGER NOT NULL REFERENCES Volunteer(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    clientid      INTEGER NOT NULL REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
    -- FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE,
    -- FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

--done
CREATE TABLE Dependant(  
    clientid		INTEGER REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    name            TEXT NOT NULL,  
    relationship    TEXT NOT NULL,
    PRIMARY KEY (clientid,name)
);

--done
CREATE TABLE Foodbank(  
    address         TEXT PRIMARY KEY NOT NULL,
    phonenumber		TEXT NOT NULL,
    email           TEXT NOT NULL,
    hours           TEXT NOT NULL,
    funds           INTEGER NOT NULL
);

-- CREATE TABLE Food(  
--     barcode         INTEGER PRIMARY KEY NOT NULL,
--     name		    TEXT NOT NULL,
--     quantity        INTEGER NOT NULL,
--     expiraydate     TEXT NOT NULL,
--     foodbank        TEXT NOT NULL
--     -- FOREIGN KEY(foodbank) REFERENCES Foodbank(address) ON UPDATE CASCADE
-- );


CREATE TABLE MaxRequests(
    famSize     INTEGER PRIMARY KEY UNIQUE,
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
    clientid        INTEGER NOT NULL REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    volunteerid     INTEGER REFERENCES Volunteer(accountid) ON UPDATE CASCADE ON DELETE CASCADE
    -- FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE ON DELETE CASCADE,
    -- FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
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
    suppliername    TEXT NOT NULL
    -- FOREIGN KEY(adminid) REFERENCES Admin(id) ON UPDATE CASCADE,
    -- FOREIGN KEY(suppliername) REFERENCES Supplier(name) ON UPDATE CASCADE
);

CREATE TABLE Supplies(
    suppliername    TEXT NOT NULL,
    foodbarcode     INTEGER NOT NULL
    -- FOREIGN KEY(suppliername) REFERENCES Supplier(name) ON UPDATE CASCADE,
    -- FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);

CREATE TABLE Donates(
    donorid         INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL
    -- FOREIGN KEY(donorid) REFERENCES Donor(id) ON UPDATE CASCADE,
    -- FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);

CREATE TABLE Prepares(
    volunteerid     INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL
    -- FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE,
    -- FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);

CREATE TABLE Takes(
    clientid        INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL
    -- FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    -- FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);

--done
CREATE TABLE Foodstore(
    refcode     INTEGER NOT NULL,
    foodname    TEXT NOT NULL,
    quantity    INTEGER NOT NULL,
    expirydate        TEXT NOT NULL,
    address     TEXT NOT NULL REFERENCES Foodbank(address) ON UPDATE CASCADE ON DELETE CASCADE
);
