
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
	accountid		INTEGER PRIMARY KEY UNIQUE REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Client(
    income 		    INTEGER,
	accountid		INTEGER PRIMARY KEY UNIQUE REFERENCES Account(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE DietaryRestrictions(
    accountid		INTEGER PRIMARY KEY UNIQUE REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    dietaryrestriction TEXT
);

CREATE TABLE Reasons(
    clientid 		INTEGER PRIMARY KEY NOT NULL,
    reason	    TEXT NOT NULL
    -- FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Appointment(
    id 		        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    time		    TEXT NOT NULL,
    volunteerid     INTEGER NOT NULL,
    clientid        INTEGER NOT NULL
    -- FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE,
    -- FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Dependant(  
    clientid		INTEGER PRIMARY KEY UNIQUE REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE,
    name            TEXT NOT NULL,
    relationship    TEXT NOT NULL
);

CREATE TABLE Foodbank(  
    address         TEXT PRIMARY KEY NOT NULL,
    phonenumber		TEXT NOT NULL,
    email           TEXT NOT NULL,
    hours           TEXT NOT NULL,
    funds           REAL NOT NULL
);

CREATE TABLE Food(  
    barcode         INTEGER PRIMARY KEY NOT NULL,
    name		    TEXT NOT NULL,
    quantity        INTEGER NOT NULL,
    expiraydate     TEXT NOT NULL,
    foodbank        TEXT NOT NULL
    -- FOREIGN KEY(foodbank) REFERENCES Foodbank(address) ON UPDATE CASCADE
);

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
    volunteerid     INTEGER,
    clientid        INTEGER NOT NULL,
    date            TEXT
    -- FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE ON DELETE CASCADE,
    -- FOREIGN KEY(clientid) REFERENCES Client(accountid) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Donor(
    id 		        INTEGER PRIMARY KEY NOT NULL,
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

CREATE TABLE Foodstore(
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
    cannedMeat      INTEGER NOT NULL
);
