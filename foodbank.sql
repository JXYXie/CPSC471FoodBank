
PRAGMA foreign_keys = ON;

CREATE TABLE Admin(
    id				INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            TEXT,
    phonenumber		TEXT
);

CREATE TABLE Volunteer(
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            TEXT,
    phonenumber		TEXT,
    availability    TEXT,
    managerid       INTEGER,
    FOREIGN KEY(managerid) REFERENCES Admin(id) ON UPDATE CASCADE
);

CREATE TABLE Client( 
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            TEXT,
    income 		    INTEGER,
    accountid 	    INTEGER,
    FOREIGN KEY(accountid) REFERENCES Client(id) ON UPDATE CASCADE
);

CREATE TABLE Account(
    username  	    TEXT PRIMARY KEY NOT NULL,
    email 		    TEXT NOT NULL,
    accesslevel	    INTEGER,
    password		TEXT NOT NULL,
    userid          INTEGER NOT NULL,
    FOREIGN KEY(userid) REFERENCES Client(id) ON UPDATE CASCADE,
    FOREIGN KEY(userid) REFERENCES Volunteer(id) ON UPDATE CASCADE,
    FOREIGN KEY(userid) REFERENCES Admin(id) ON UPDATE CASCADE
);

CREATE TABLE DietaryRestrictions(
    clientid 		        INTEGER PRIMARY KEY NOT NULL,
    dietaryrestriction	    TEXT NOT NULL,
    FOREIGN KEY(clientid) REFERENCES Client(id) ON UPDATE CASCADE
);

CREATE TABLE Reasons(
    clientid 		INTEGER PRIMARY KEY NOT NULL,
    reason		    TEXT NOT NULL,
    FOREIGN KEY(clientid) REFERENCES Client(id) ON UPDATE CASCADE
);

CREATE TABLE Appointment(
    id 		        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    time		    TEXT NOT NULL,
    volunteerid     INTEGER NOT NULL,
    clientid        INTEGER NOT NULL,
    FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE,
    FOREIGN KEY(clientid) REFERENCES Client(id) ON UPDATE CASCADE
);

CREATE TABLE Dependant(  
    clientid        INTEGER NOT NULL,
    name            TEXT NOT NULL,
    relationship    TEXT NOT NULL,
    FOREIGN KEY(clientid) REFERENCES Client(id) ON UPDATE CASCADE
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
    foodbank        TEXT NOT NULL,
    FOREIGN KEY(foodbank) REFERENCES Foodbank(address) ON UPDATE CASCADE
);

CREATE TABLE RequestForm(
    id 		        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    priority		INTEGER NOT NULL,
    volunteerid     INTEGER NOT NULL,
    clientid        INTEGER NOT NULL,
    FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE,
    FOREIGN KEY(clientid) REFERENCES Client(id) ON UPDATE CASCADE
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
    suppliername    TEXT NOT NULL,
    FOREIGN KEY(adminid) REFERENCES Admin(id) ON UPDATE CASCADE,
    FOREIGN KEY(suppliername) REFERENCES Supplier(name) ON UPDATE CASCADE
);

CREATE TABLE Supplies(
    suppliername    TEXT NOT NULL,
    foodbarcode     INTEGER NOT NULL,
    FOREIGN KEY(suppliername) REFERENCES Supplier(name) ON UPDATE CASCADE,
    FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);

CREATE TABLE Donates(
    donorid         INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL,
    FOREIGN KEY(donorid) REFERENCES Donor(id) ON UPDATE CASCADE,
    FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);

CREATE TABLE Prepares(
    volunteerid     INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL,
    FOREIGN KEY(volunteerid) REFERENCES Volunteer(id) ON UPDATE CASCADE,
    FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);

CREATE TABLE Takes(
    clientid        INTEGER NOT NULL,
    foodbarcode     INTEGER NOT NULL,
    FOREIGN KEY(clientid) REFERENCES Client(id) ON UPDATE CASCADE,
    FOREIGN KEY(foodbarcode) REFERENCES Food(barcode) ON UPDATE CASCADE
);


