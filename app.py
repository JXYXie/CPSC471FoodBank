
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

currentUser = 0
#where 1 = client, 2 = user, 3 = admin

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/admin')
def admin():
	global currentUser
	if currentUser==3:
		return render_template('admin.html')
	else:
		return render_template('index.html')

#############garbage

@app.route('/loginClient')
def loginClient():
	currentUser = 1
	return render_template('index.html')
	








####################

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/reqform')
def reqform():
	return render_template('reqform.html')

@app.route('/addAdmin')
def addAdmin():
	return render_template('addAdmin.html')

@app.route('/addAppointment')
def addAppointment():
	return render_template('addAppointment.html')

@app.route('/addDonor')
def addDonor():
	return render_template('addDonor.html')

@app.route('/addFunds')
def addFunds():
	return render_template('addFunds.html')

@app.route('/addInventory')
def addInventory():
	return render_template('addInventory.html')

@app.route('/addSupplier')
def addSupplier():
	return render_template('addSupplier.html')

@app.route('/addVolunteer')
def addVolunteer():
	return render_template('addVolunteer.html')

@app.route('/editAdmin')
def editAdmin():
	return render_template('editAdmin.html')

@app.route('/editAppointment')
def editAppointment():
	return render_template('editAppointment.html')

@app.route('/editClient')
def editClient():
	return render_template('editClient.html')

@app.route('/editInventory')
def editInventory():
	return render_template('editInventory.html')

@app.route('/editVolunteer')
def editVolunteer():
	return render_template('editVolunteer.html')

@app.route('/viewAdmin')
def viewAdmin():
	return render_template('viewAdmin.html')

@app.route('/viewAppointment')
def viewAppointment():
	return render_template('viewAppointment.html')

@app.route('/viewClient')
def viewClient():
	return render_template('viewClient.html')

@app.route('/viewInventory')
def viewInventory():
	return render_template('viewInventory.html')

@app.route('/viewVolunteer')
def viewVolunteer():
	return render_template('viewVolunteer.html')


@app.route('/register', methods=['POST'])
def addClientUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()


	c.execute(
		"INSERT INTO Client (name,email,username,  password, income) VALUES ('{name}','{email}','{username}', '{password}', '{income}')".format(
			name=request.form['name'],
			#phonenumber=request.form['phone'],
			#removed phone number not in site form removed from sql as well
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password'],
			income=request.form['income']))
	t=(request.form['name'])
	temp = (t,)
	c.execute('SELECT * FROM Client WHERE name=?', temp)
	key = c.fetchone()[0]

# CREATE TABLE Dependant(  
#     clientid        INTEGER NOT NULL,
#     name            TEXT NOT NULL,
#     relationship    TEXT NOT NULL,
#     FOREIGN KEY(clientid) REFERENCES Client(id) ON UPDATE CASCADE
# );


	#need to do this for all dependents?  how to for loop lmao
	c.execute(
		"INSERT INTO Dependant (clientid,name,relationship) VALUES ('{clientid}','{name}','{relationship}')".format(
			clientid=key,
			name=request.form['dname1'],
			relationship=request.form['relation1']))


# CREATE TABLE Client( 
#     id              INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name            TEXT,
#     phonenumber		TEXT,
#     email 		    TEXT NOT NULL,
#     username  	    TEXT NOT NULL UNIQUE,
#     password		TEXT NOT NULL,
#     income 		    INTEGER
# );


	
	conn.commit()
	conn.close()
	return redirect('/')

@app.route('/addAdminUser', methods=['POST'])
def addAdminUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	# TODO: get the data from form
	# username = request.form['username']



# 	CREATE TABLE Admin(
#     id				INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name            TEXT,
#     phonenumber		TEXT,
#     email 		    TEXT NOT NULL,
#     username  	    TEXT NOT NULL UNIQUE,
#     password		TEXT NOT NULL
# );


	# TODO: put datat in
	c.execute(
		"INSERT INTO Admin (name, phonenumber,email,username,  password) VALUES ('{name}', '{phonenumber}','{email}','{username}', '{password}')".format(
			name=request.form['name'],
			phonenumber=request.form['phone'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password']))
	
	conn.commit()
	conn.close()
	return redirect('/admin')


# 	CREATE TABLE Volunteer(
#     id              INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name            TEXT,
#     phonenumber		TEXT,
#     email 		    TEXT NOT NULL,
#     username  	    TEXT NOT NULL UNIQUE,
#     password		TEXT NOT NULL,
#     availability    TEXT,
#     managerid       INTEGER,
#     FOREIGN KEY(managerid) REFERENCES Admin(id) ON UPDATE CASCADE
# );
@app.route('/addVolunteerUser', methods=['POST'])
def addVolunteerUser():
	# open connection
	conn = sqlite3.connect('foodbank.db')
	c = conn.cursor()

	c.execute(
		"INSERT INTO Volunteer (name, phonenumber,email,username,  password,availability,managerid) VALUES ('{name}', '{phonenumber}','{email}','{username}', '{password}','{availability}','{managerid}')".format(
			name=request.form['name'],
			phonenumber=request.form['phone'],
			email=request.form['email'],
			username=request.form['username'],
			password=request.form['password'],
			availability=request.form['availability'],
			managerid=request.form['managerid']))
	
	conn.commit()
	conn.close()
	return redirect('/admin')