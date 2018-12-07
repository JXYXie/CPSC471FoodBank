
PRAGMA foreign_keys = ON;

CREATE TABLE Account(
  id    		INTEGER PRIMARY KEY AUTOINCREMENT,
  username  	TEXT,
  email 		TEXT,
  accesslevel	INTEGER,
  password		TEXT
);

CREATE TABLE Client( 
  id    		INTEGER PRIMARY KEY,  
  name  		TEXT,
  income 		INTEGER,
  accountid 	INTEGER REFERENCES Client(id) ON UPDATE CASCADE 
);

CREATE TABLE Reasons(
  id     		INTEGER,  
  name			TEXT,
  reason   		TEXT,   
  clientid 		INTEGER REFERENCES Client(id) ON UPDATE CASCADE 
);


CREATE TABLE DietaryRestrictions(  
  id     		INTEGER,  
  name			TEXT,
  reason   		TEXT,   
  clientid 		INTEGER REFERENCES Client(id) ON UPDATE CASCADE 
);

CREATE TABLE Dependant(  
  id     		INTEGER,  
  name			TEXT,
  relationship  TEXT,  
  clientid 		INTEGER REFERENCES Client(id) ON UPDATE CASCADE 
);
